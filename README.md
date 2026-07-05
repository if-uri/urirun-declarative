# urirun-declarative


## AI Cost Tracking

![PyPI](https://img.shields.io/badge/pypi-costs-blue) ![Version](https://img.shields.io/badge/version-0.1.1-blue) ![Python](https://img.shields.io/badge/python-3.9+-blue) ![License](https://img.shields.io/badge/license-Apache--2.0-green)
![AI Cost](https://img.shields.io/badge/AI%20Cost-$0.01-orange) ![Human Time](https://img.shields.io/badge/Human%20Time-5.4h-blue) ![Model](https://img.shields.io/badge/Model-openrouter%2Fqwen%2Fqwen3--coder--next-lightgrey)

- 🤖 **LLM usage:** $0.0132 (2 commits)
- 👤 **Human dev:** ~$538 (5.4h @ $100/h, 30min dedup)

Generated on 2026-07-05 using [openrouter/qwen/qwen3-coder-next](https://openrouter.ai/qwen/qwen3-coder-next)

---

Define **urirun connector routes declaratively** — a spec dict (scheme, target, routes with
method/path/schema) becomes typed URI bindings with **no Python handler code**. The urirun `fetch`
adapter then resolves each route. Extracted from `urirun.connectors.declarative` as a standalone,
dependency-free package.

Pure stdlib (`pathlib`, `typing`) — **no `urirun` dependency** — so a declarative connector
(e.g. `urirun-connector-ksef`) can depend on just this, not the whole backend.

## Why it's its own package

`extraction_audit.py` reports it a clean leaf (zero urirun imports, stdlib only). It is a distinct,
reusable capability — spec → bindings — consumed by declarative connectors. Same lift case as
`urirun-cdp` / `urirun-uinput` / `urirun-openapi-import`.

## Install

```bash
pip install -e .          # editable, from this repo
```

## Use

```python
from urirun_declarative import declarative

spec = declarative.load_spec("ksef.routes.yaml")
bindings = declarative.bindings_from_spec(spec)
```

## Back-compat

The old import path still works via a re-export shim in the urirun package:

```python
from urirun.connectors import declarative   # → urirun_declarative.declarative (sys.modules shim)
```

A connector that imports this at module top (e.g. ksef) declares `urirun-declarative` in its own
dependencies, so it is installed wherever that connector runs.

## Tests

```bash
PYTHONPATH=../urirun/adapters/python python -m pytest tests/ -q
```

## License

Licensed under Apache-2.0.
