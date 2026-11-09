import argparse
from pathlib import Path
import shutil


CATEGORIES = {
    "images": {".gif", ".jpeg", ".jpg", ".png"},
    "documents": {".docx", ".md", ".pdf", ".txt"},
    "spreadsheets": {".csv", ".xlsx"},
}


def category_for(file_path: Path) -> str:
    raise NotImplementedError


def plan_moves(folder: Path) -> list[tuple[Path, Path]]:
    raise NotImplementedError


def apply_moves(moves: list[tuple[Path, Path]]) -> None:
    raise NotImplementedError


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize files by type.")
    parser.add_argument("folder", type=Path)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Move files instead of only previewing the changes.",
    )
    args = parser.parse_args()

    if not args.folder.is_dir():
        parser.error(f"not a folder: {args.folder}")

    moves = plan_moves(args.folder)
    for source, destination in moves:
        print(f"{source} -> {destination}")

    if args.apply:
        apply_moves(moves)


if __name__ == "__main__":
    main()