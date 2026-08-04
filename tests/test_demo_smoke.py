import os
import subprocess
from pathlib import Path


def run_cmd(cmd, *, cwd=None, env=None):
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=cwd, env=env)
    if res.returncode != 0:
        raise AssertionError(f"Command failed ({cmd}):\n{res.stdout}")
    return res.stdout


def test_vhir_cli_smoke(tmp_path: Path) -> None:
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir()

    env = os.environ.copy()
    env["VHIR_CASES_DIR"] = str(cases_dir)

    # Check `vhir --version` is available after install
    out = run_cmd(["vhir", "--version"], env=env)
    assert "vhir" in out.lower()

    # Initialize a demo case and ensure it appears in the list
    run_cmd(["vhir", "case", "init", "demo-case"], env=env)
    out = run_cmd(["vhir", "case", "list"], env=env)
    assert "demo-case" in out
