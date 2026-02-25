# quest-pp-calibration

This project focuses on the calibration of data from the permeation probes used in QUEST. It primarily includes the following:

- **Calculation of the pumping speed** of the permeation probe.
- **Conversion of QMS ion current** into permeation flux.
- **Calculation of the recombination coefficient (\(k_u\))** on the metal membrane surface.

## Venv

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

**macOS / Linux (bash)**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install

From the repository root:

```bash
pip install -e .
```

Or install `docs` to run `mkdocs`
```bash
python -m pip install -e ".[docs]"
```

```bash
python -m pip install -e ".[docs,dev]"
```