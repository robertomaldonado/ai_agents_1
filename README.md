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

### Configure OpenAI

You can provide your API key via any of the following methods (priority order):

1. Environment variable:

```bash
export OPENAI_API_KEY="sk-your-key"
python main.py
```

2. .env file (auto-loaded): create a file named `.env` in the project root:

```bash
echo "OPENAI_API_KEY=sk-your-key" > .env
```

3. Key file: save your API key to a file, default `.openai_key`:

```bash
echo "sk-your-key" > .openai_key
python main.py
```

You can change the key file path by setting `OPENAI_API_KEY_FILE`.

You'll be prompted for a message; the app will call OpenAI (`gpt-4o-mini`) and print the assistant's reply.

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
