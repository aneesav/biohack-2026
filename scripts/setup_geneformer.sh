#!/usr/bin/env bash
# Downloads the Geneformer-V1-10M checkpoint + library code from Hugging Face
# (only ~50MB total: the smallest available Geneformer checkpoint) and installs
# the library into the current Python environment.
#
# Geneformer isn't published on PyPI -- the maintainers only ship it from the
# Hugging Face repo, bundled together with several much larger model
# checkpoints. We use allow_patterns so we only pull the V1-10M weights and
# the library code, not the multi-GB V2 checkpoints sitting next to them.
set -euo pipefail

cd "$(dirname "$0")/.."

python - <<'PY'
from huggingface_hub import snapshot_download

path = snapshot_download(
    repo_id="ctheodoris/Geneformer",
    allow_patterns=[
        "Geneformer-V1-10M/*",
        "geneformer/*",
        "setup.py",
        "pyproject.toml",
        "requirements.txt",
        "README.md",
    ],
    local_dir="vendor/geneformer_repo",
)
print(f"Downloaded Geneformer to {path}")
PY

pip install -e vendor/geneformer_repo
echo "Geneformer installed. Verify with: python -c 'import geneformer; print(geneformer.__file__)'"
