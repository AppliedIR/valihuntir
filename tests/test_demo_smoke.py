import subprocess
from pathlib import Path


def run_cmd(cmd, *, cwd=None):
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=cwd)
    if res.returncode != 0:
        raise AssertionError(f"Command failed ({cmd}):\n{res.stdout}")
    return res.stdout


def test_vhir_cli_smoke(tmp_path: Path) -> None:
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir()

    # Check `vhir --version` is available after install
    out = run_cmd(["vhir", "--version"])
    assert "vhir" in out.lower()

    # Initialize a demo case and ensure it appears in the list
    run_cmd(["vhir", "case", "init", "demo-case", "--cases-dir", str(cases_dir)])
    out = run_cmd(["vhir", "case", "list", "--cases-dir", str(cases_dir)])
    assert "demo-case" in out
