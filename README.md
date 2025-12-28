# Python Study Workspace

This workspace contains simple Python scripts and a `requirements.txt` for dependencies.

## Structure

- `functions.py`: Utility functions and small demonstrations previously in `def.py`.
- `hello.py`: Basic data structures and HTTP request examples (uses `requests`).
- `my_math.py`: Math/random/json/datetime examples; renamed from `math.py` to avoid shadowing the Python standard library `math` module.
- `requirements.txt`: Pinned dependencies for `requests` and its transitive libs.
- `.venv/`: Local virtual environment (recommended for installing dependencies).

## Why the renames
- Avoid reserved keywords: `def.py` cannot be imported; moved to `functions.py`.
- Fix typo: `hellow.py` → `hello.py`.
- Prevent stdlib shadowing: `math.py` → `my_math.py`.

## Setup
```bash
# Activate your venv (PowerShell)
. .\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run examples
python hello.py
python my_math.py
python functions.py
```

## Notes
- If you import modules between files, prefer explicit names like `import my_math as mm` rather than shadowing stdlib modules.
- Keep scripts focused; consider adding tests as the next step.
