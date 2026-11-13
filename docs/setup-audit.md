# Clean-install audit

## Baseline

Audited on 2026-11-13 against commit `bbf2913` on Linux with Python 3.12.3
and GNU Make. The README was the only setup document; no dependencies had
been installed by project setup. A separate local clone and a new virtual
environment were used, without system site-packages.

The original setup commands and examples were run as written:

| Step | Observed result |
| --- | --- |
| `python -m venv .venv` and `source .venv/bin/activate` | Passed on this Linux host. |
| `pip install -e .` | Passed. |
| `pip install -e ".[test]"` and `pytest` | Passed: 65 tests. |
| README Python quick-start example | Passed: `4.516` seconds, `100.0` joules, `1.5 м/с`. |
| `physex --constants` | Passed: 17 constants. |
| `physex --ke 2.0 10.0` | Passed: `Кинетическая энергия: 100 Дж`. |

No documented Linux command failed. The missing steps and portability issues
below were found by comparing that path with what a newcomer needs before
and after those commands; they are not claimed as failures of the original
Linux walkthrough.

## Findings and changes

| Finding | Evidence / impact | Resolution |
| --- | --- | --- |
| No clone or working-directory step | The first command assumed an existing checkout in its root. | Added the repository URL and `cd PhysEX`. |
| No prerequisite list or minimum Python version | `pyproject.toml` requires Python 3.9+, but the README did not say so. A bare `python` command is not provided by every OS. | Listed Python, pip, venv, Git, network access, and optional Make; separated Unix and Windows commands. |
| Windows activation was an ambiguous comment on a `source` command | PowerShell and cmd.exe require different activation commands; `source` is a Unix shell command. | Added shell-specific commands and a no-activation PowerShell alternative. Windows/macOS were not available for execution in this audit. |
| Bare `pip` and `pytest` rely on PATH | They may select a different interpreter from the intended Python. | Used `python -m pip` and `python -m pytest`. |
| Makefile could not select a Python interpreter | With the venv absent from PATH, `PATH=/usr/bin:/bin make test PYTHON="$PWD/.venv/bin/python"` failed with `make: pytest: No such file or directory` (exit 2). The original Makefile ignored `PYTHON`. | Added overridable `PYTHON` and module invocations for installation, tests, and the CLI. |
| No expected output or dependency explanation | Newcomers could not readily distinguish a working CLI/test run or know why pytest was missing after the basic install. | Added CLI output, test count, editable-install explanation, and `[test]` guidance. |
| No package-build instructions | `python -m build` after the original test setup failed with `No module named build` (exit 1); the build frontend is not a runtime or test dependency. | Added optional frontend installation, build command, and expected artifacts; kept runtime dependencies unchanged. |
| Deprecated license metadata in the optional build | The first build succeeded but setuptools warned that the license table and license classifier are deprecated. | Switched to SPDX `license = "MIT"` and explicit `license-files`; raised the backend minimum to 77.0.3 to support that metadata. See [setuptools documentation](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html). |
| No recovery guidance | Missing venv/pip, inactive environments, and externally managed Python installations had no documented remedies. | Added focused troubleshooting without recommending sudo pip or disabling system protections. |

The initial pip runs also warned that the sandbox's configured pip cache was
not writable. Installation still succeeded with caching disabled. This is a
host-specific warning, not a repository setup defect; the verification rerun
uses a writable temporary cache.

## Verification of the revised path

The revised Linux instructions are verified in a second clean checkout and
virtual environment. Verification includes editable installation, the Python
quick-start and both CLI examples, all tests, optional Make commands (including
an explicit interpreter without activation), isolated wheel/sdist builds, and
installation of the wheel into another new environment. The wheel is tested
outside the source checkout to avoid accidentally importing source files.

Results: **65 tests passed** in editable and wheel installations; CLI examples
and all three Make targets passed, with and without activation. Both distribution
artifacts built successfully. The final build emitted no license-deprecation
warnings. macOS, Windows, and Python versions other than 3.12 were not run.
