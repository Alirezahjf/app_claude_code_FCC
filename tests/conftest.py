import os
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("FCC_DATA_DIR", os.path.join(tempfile.gettempdir(), "fcc-test-data"))
os.environ.setdefault("CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC", "1")


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return ROOT


@pytest.fixture()
def tmp_config(tmp_path):
    from fcc import config as config_module
    from fcc import paths

    os.environ["FCC_DATA_DIR"] = str(tmp_path / "data")
    paths._current = None  # type: ignore[attr-defined]
    config_module._current = None
    config = config_module.load()
    yield config
    config_module._current = None
