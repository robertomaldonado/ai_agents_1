## Agentic

### Overview

Minimal Python project scaffold. Update this README as the project evolves.

### Requirements

- **Python**: 3.13+

### Setup

1. Create a virtual environment:
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell): `py -3 -m venv .venv; .venv\\Scripts\\Activate.ps1`
2. Upgrade pip and install dependencies:
   - `python -m pip install --upgrade pip`
   - `pip install -e .` (optional, if you later add packaging config)

If you add runtime dependencies to `pyproject.toml` under `project.dependencies`, install them with:
`pip install -r requirements.txt` (if you maintain one) or `pip install .`

### Run

```bash
python main.py
```

### Development

- Format/lint (add your preferred tools, e.g., ruff/black):
  - Example: `pip install ruff black`
  - Format: `black .`
  - Lint: `ruff check .`
- Tests (if using pytest):
  - `pip install pytest`
  - `pytest -q`

### Project Structure

```text
.
├── main.py            # Entry point
├── pyproject.toml     # Project metadata and dependencies
└── README.md          # Documentation
```

### License

Add a license (e.g., MIT) if this will be public.
