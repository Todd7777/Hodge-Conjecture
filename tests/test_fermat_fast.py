"""Cross-check the compiled scanner scripts/fermat_fast.c against hodge.fermat.

Skipped when no C compiler is available.
"""
import shutil
import subprocess
from pathlib import Path

import pytest

from hodge import fermat

ROOT = Path(__file__).resolve().parents[1]
CC = shutil.which("gcc") or shutil.which("cc")

pytestmark = pytest.mark.skipif(CC is None, reason="no C compiler")


@pytest.fixture(scope="module")
def fermat_fast(tmp_path_factory):
    exe = tmp_path_factory.mktemp("bin") / "fermat_fast"
    subprocess.run([CC, "-O2", "-o", str(exe), str(ROOT / "scripts" / "fermat_fast.c")],
                   check=True, capture_output=True)
    return exe


def run_c(exe, n, m, tmp_path):
    out = tmp_path / f"ff_{n}_{m}.txt"
    subprocess.run([str(exe), str(n), str(m), str(out)], check=True, capture_output=True)
    fields, orbits = {}, []
    for line in out.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if parts[0][0].isdigit():
            orbits.append(tuple(int(x) for x in parts))
        else:
            fields[parts[0]] = parts[1]
    return fields, orbits


@pytest.mark.parametrize("n,m", [(2, 9), (2, 12), (4, 12), (4, 25), (4, 33), (6, 12), (6, 25)])
def test_c_matches_python(fermat_fast, tmp_path, n, m):
    fields, orbits = run_c(fermat_fast, n, m, tmp_path)
    ref = fermat.analyze(n, m)
    assert int(fields["dim_hodge_classes"]) == ref["dim_hodge_classes"]
    assert int(fields["dim_indecomposable"]) == ref["dim_indecomposable"]
    assert int(fields["dim_decomposable"]) == ref["dim_decomposable"]
    assert int(fields["b_prim"]) == ref["b_prim"]
    assert orbits == [tuple(o) for o in ref["indecomposable_orbits"]]
