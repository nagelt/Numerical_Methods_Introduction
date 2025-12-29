python3 - <<'EOF'
import re
import json
import nbformat
from nbformat.reader import NotJSONError
from pathlib import Path

TARGET_LINE = "#HIDDEN"
SKIP_DIRS = {".virtual_documents", ".ipynb_checkpoints"}

# Exact image src that identifies the old header you want to replace:
MATCH_IMG_SRC = "https://github.com/nagelt/Teaching_Scripts/raw/9d9e29ecca4b04eaf7397938eacbf116d37ddc93/Images/TUBAF_Logo_blau.png"

header = Path("header.html").read_text(encoding="utf-8")

def remove_hidden_lines(text: str) -> str:
    lines = text.splitlines(True)  # keep line endings
    return "".join(line for line in lines if line.strip() != TARGET_LINE)

def first_cell_has_exact_img_src(md: str, src: str) -> bool:
    """
    True if md contains an <img ... src="src" ...> (single or double quotes),
    allowing arbitrary whitespace/attribute ordering.
    """
    src_escaped = re.escape(src)
    pattern = rf"<img\b[^>]*\bsrc\s*=\s*(['\"])({src_escaped})\1"
    return re.search(pattern, md, flags=re.IGNORECASE | re.DOTALL) is not None

for nb_path in Path(".").rglob("*.ipynb"):
    if any(part in SKIP_DIRS for part in nb_path.parts):
        continue

    print(f"Processing notebook: {nb_path}")

    try:
        nb = nbformat.read(nb_path, as_version=4)
    except (NotJSONError, json.JSONDecodeError) as e:
        print(f"  → skipped (not a real ipynb JSON): {e.__class__.__name__}")
        continue
    except Exception as e:
        print(f"  → skipped (read error): {e}")
        continue

    modified = False

    # 1) Line-based removal of "#HIDDEN" across all cells
    for cell in nb.cells:
        src = getattr(cell, "source", None)
        if isinstance(src, str):
            new_src = remove_hidden_lines(src)
            if new_src != src:
                cell.source = new_src
                modified = True

    # 2) Replace first cell ONLY if it's markdown and contains the exact identifying img src
    if nb.cells:
        first = nb.cells[0]
        if getattr(first, "cell_type", None) == "markdown" and isinstance(getattr(first, "source", None), str):
            if first_cell_has_exact_img_src(first.source, MATCH_IMG_SRC):
                if first.source != header:
                    nb.cells[0] = nbformat.v4.new_markdown_cell(header)
                    modified = True

    if modified:
        nbformat.write(nb, nb_path)
        print("  → Updated\n")
    else:
        print("  → no changes\n")
EOF
