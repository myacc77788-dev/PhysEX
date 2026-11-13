import pytest

from physex.cli import main
from physex.constants import all_constants


def test_no_arguments_prints_help(capsys):
    assert main([]) == 0
    captured = capsys.readouterr()
    assert "usage: physex" in captured.out
    assert "--ke MASS VELOCITY" in captured.out
    assert captured.err == ""


def test_help_exits_successfully(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--help"])
    assert exc.value.code == 0
    assert "usage: physex" in capsys.readouterr().out


@pytest.mark.parametrize("flag", ["-c", "--constants"])
def test_constants_output(flag, capsys):
    assert main([flag]) == 0
    captured = capsys.readouterr()
    constants = sorted(all_constants(), key=lambda c: c.name)
    lines = captured.out.splitlines()
    assert len(lines) == len(constants)
    for line, constant in zip(lines, constants):
        assert line.split()[0] == constant.symbol
        assert constant.name in line
        assert line.endswith(f"= {constant.value:g} {constant.unit}")
    assert captured.err == ""


@pytest.mark.parametrize(
    "mass, velocity, energy",
    [("2", "10", "100"), ("2.5", "-4", "20"), ("0", "10", "0")],
)
def test_kinetic_energy_output(mass, velocity, energy, capsys):
    assert main(["--ke", mass, velocity]) == 0
    captured = capsys.readouterr()
    assert captured.out == f"Кинетическая энергия: {energy} Дж\n"
    assert captured.err == ""


@pytest.mark.parametrize(
    "argv, error",
    [
        (["--ke"], "expected 2 arguments"),
        (["--ke", "2"], "expected 2 arguments"),
        (["--ke", "bad", "10"], "invalid float value"),
        (["--ke", "2", "bad"], "invalid float value"),
        (["--ke", "2", "10", "20"], "unrecognized arguments"),
        (["--unknown"], "unrecognized arguments"),
    ],
)
def test_invalid_arguments_exit_without_calculation(argv, error, capsys):
    with pytest.raises(SystemExit) as exc:
        main(argv)
    assert exc.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "usage: physex" in captured.err
    assert error in captured.err


def test_main_reads_process_arguments(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["physex", "--ke", "2", "10"])
    assert main() == 0
    assert capsys.readouterr().out == "Кинетическая энергия: 100 Дж\n"
