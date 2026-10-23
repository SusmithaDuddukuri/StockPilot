"""Count first-party production source lines using explicit exclusions.

Usage: python tools/loc_audit.py [repository-root]
This is a transparent local estimate, not a replacement for the submission evaluator.
"""
from pathlib import Path
import sys

SOURCE_SUFFIXES = {'.py', '.js', '.ts', '.tsx', '.jsx', '.java', '.go', '.rs', '.css', '.html'}
EXCLUDED_PARTS = {
    '.git', '.venv', 'venv', 'node_modules', 'coverage', 'dist', 'build',
    '__pycache__', 'tests', 'test', 'generated', 'fixtures', 'vendor',
}


def is_production_source(path: Path) -> bool:
    if path.suffix.lower() not in SOURCE_SUFFIXES:
        return False
    return not any(part.lower() in EXCLUDED_PARTS for part in path.parts)


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
    files = sorted(path for path in root.rglob('*') if path.is_file() and is_production_source(path.relative_to(root)))
    totals = {}
    total_lines = 0
    for path in files:
        try:
            count = len(path.read_text(encoding='utf-8').splitlines())
        except (UnicodeDecodeError, OSError):
            continue
        totals[path.suffix.lower()] = totals.get(path.suffix.lower(), 0) + count
        total_lines += count
    print(f'Root: {root}')
    print(f'Production source files: {len(files)}')
    print(f'Production source LOC: {total_lines:,}')
    for suffix, count in sorted(totals.items()):
        print(f'{suffix}: {count:,}')
    print('Note: evaluator-specific generated-file heuristics may differ from this audit.')


if __name__ == '__main__':
    main()
