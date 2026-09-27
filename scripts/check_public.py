"""Check the exact files Git would see before publishing; never print file contents."""

from __future__ import annotations

import re
import stat
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PUBLIC_FILES = frozenset(
    {
        ".gitignore",
        "README.md",
        "ATTRIBUTION.md",
        "docs/PRIVACY.md",
        "docs/RUNBOOK.md",
        "prompts/create-assistant.md",
        "prompts/assistant-system.md",
        "prompts/topic-bootstrap.md",
        "prompts/handoff.md",
        "examples/synthetic-dialogue.md",
        "scripts/check_public.py",
    }
)

PATTERNS = {
    "微信账号形态": re.compile(r"wxid_[A-Za-z0-9_-]{6,}", re.I),
    "手机号形态": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    "邮箱形态": re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"),
    "本机 Windows 路径": re.compile(r"\b[A-Za-z]:[\\/]"),
    "密钥形态": re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    "疑似硬编码凭据": re.compile(
        r"(?i)(?:api[_-]?key|token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_-]{16,}"
    ),
}


def git(*args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def main() -> int:
    if not (ROOT / ".git").is_dir():
        print("检查未运行：项目尚未初始化本地 Git。")
        return 2

    result = git("ls-files", "--cached", "--others", "--exclude-standard", "-z")
    if result.returncode:
        print("检查未运行：无法获得 Git 的可提交文件清单。")
        return 2

    candidates = {
        name.decode("utf-8", "surrogateescape").replace("\\", "/")
        for name in result.stdout.split(b"\0")
        if name
    }
    unexpected = candidates - PUBLIC_FILES
    missing = PUBLIC_FILES - candidates
    if unexpected or missing:
        print(
            "检查未通过：可提交清单与白名单不同；"
            f"多出 {len(unexpected)} 个，缺少 {len(missing)} 个。"
        )
        return 1

    for local_only in ("toolchain/WeChatMsg/readme.md", "toolchain/venv/Scripts/python.exe"):
        if git("check-ignore", "-q", local_only).returncode != 0:
            print("检查未通过：本地工具目录未被 Git 忽略。")
            return 1

    total_bytes = 0
    for relative in sorted(PUBLIC_FILES):
        path = ROOT / relative
        if not path.is_file() or path.is_symlink():
            print("检查未通过：公开文件缺失或包含文件链接。")
            return 1
        metadata = path.lstat()
        reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        if getattr(metadata, "st_file_attributes", 0) & reparse_flag:
            print("检查未通过：公开文件包含重解析点。")
            return 1
        if not path.resolve(strict=True).is_relative_to(ROOT):
            print("检查未通过：公开文件指向项目之外。")
            return 1
        data = path.read_bytes()
        total_bytes += len(data)
        if len(data) > 1024 * 1024 or b"\0" in data:
            print("检查未通过：公开文件过大或不是纯文本。")
            return 1
        try:
            content = data.decode("utf-8")
        except UnicodeDecodeError:
            print("检查未通过：公开文件不是 UTF-8。")
            return 1
        for category, pattern in PATTERNS.items():
            if pattern.search(relative) or pattern.search(content):
                print(f"检查未通过：发现{category}；文件内容未显示。")
                return 1

    print(f"基础检查通过：{len(PUBLIC_FILES)} 个公开文本文件，共 {total_bytes} 字节。")
    print("仍须人工审阅；本检查不会扫描未提交的本地工具或 Git 历史。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
