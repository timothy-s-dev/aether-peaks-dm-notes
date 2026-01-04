#!/usr/bin/env python3

from pathlib import Path

VAULT_ROOT = Path.cwd()
OUTPUT_FILE = VAULT_ROOT / "combined.md"

def should_include(md_file: Path) -> bool:
    # Skip the output file itself
    if md_file.resolve() == OUTPUT_FILE.resolve():
        return False

    # Skip anything inside a dot-directory (.obsidian, .git, etc.)
    if any(part.startswith(".") for part in md_file.relative_to(VAULT_ROOT).parts):
        return False

    return True

def combine_markdown(vault_root: Path, output_file: Path):
    md_files = sorted(
        p for p in vault_root.rglob("*.md")
        if should_include(p)
    )

    with output_file.open("w", encoding="utf-8") as out:
        for i, md_file in enumerate(md_files):
            relative_path = md_file.relative_to(vault_root)

            if i > 0:
                out.write("\n\n\n")

            # File path header
            out.write(f"- - -\n**{relative_path}**\n- - -\n\n")

            content = md_file.read_text(encoding="utf-8")
            out.write(content.rstrip())

    print(f"Combined {len(md_files)} files into {output_file}")

if __name__ == "__main__":
    combine_markdown(VAULT_ROOT, OUTPUT_FILE)
