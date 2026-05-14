#!/usr/bin/env python3
"""初始化四六级英语学习输出目录。

创建输出目录、复制原始语料、创建 5 个空文件，为后续 AI 填充内容做好准备。
将不确定的文件系统操作固化为脚本，减少 token 消耗并确保输出结构一致。
"""

import argparse
import shutil
import sys
from pathlib import Path

# 固定的输出文件列表（相对于输出目录）
OUTPUT_FILES = [
    "词汇表.csv",
    "关键句式.md",
    "精读笔记.md",
    "费曼练习.md",
    "墨墨卡片.txt",
]


def main():
    parser = argparse.ArgumentParser(
        description="初始化四六级英语学习输出目录"
    )
    parser.add_argument(
        "--source",
        required=True,
        help="原始英语语料文件路径",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="输出目录名（如 lupin-iii-composer-learning）",
    )
    args = parser.parse_args()

    source_path = Path(args.source).resolve()
    output_dir = Path.cwd() / args.output_dir

    # 验证源文件存在
    if not source_path.exists():
        print(f"错误：源文件不存在 — {source_path}", file=sys.stderr)
        sys.exit(1)
    if not source_path.is_file():
        print(f"错误：源路径不是文件 — {source_path}", file=sys.stderr)
        sys.exit(1)

    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ 创建目录：{output_dir}")

    # 复制原始语料
    dest_source = output_dir / "source.txt"
    shutil.copy2(source_path, dest_source)
    print(f"✓ 复制语料：source.txt ({source_path.name} → {dest_source})")

    # 创建 5 个空文件
    for filename in OUTPUT_FILES:
        filepath = output_dir / filename
        filepath.touch()
        print(f"✓ 创建文件：{filename}")

    print(f"\n目录就绪，共 {len(OUTPUT_FILES) + 1} 个文件待填充：")
    print(f"  {output_dir}/")
    print(f"  ├── source.txt")
    for f in OUTPUT_FILES:
        print(f"  ├── {f}")


if __name__ == "__main__":
    main()
