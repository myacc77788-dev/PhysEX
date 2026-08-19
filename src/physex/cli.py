"""Простая команда `physex` для вывода констант и быстрых расчётов."""

from __future__ import annotations

import argparse
import sys

from .constants import all_constants

__all__ = ["main"]


def _print_constants() -> None:
    for c in sorted(all_constants(), key=lambda x: x.name):
        print(f"{c.symbol:>4}  {c.name:<38} = {c.value:g} {c.unit}")


def _compute_kinetic(mass: float, velocity: float) -> None:
    from .energy import kinetic_energy

    print(f"Кинетическая энергия: {kinetic_energy(mass, velocity):.4g} Дж")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="physex",
        description="PhysEX — физические расчёты из командной строки.",
    )
    parser.add_argument(
        "-c", "--constants",
        action="store_true",
        help="вывести список физических констант",
    )
    parser.add_argument(
        "--ke",
        nargs=2,
        metavar=("MASS", "VELOCITY"),
        type=float,
        help="кинетическая энергия тела (масса, скорость)",
    )
    args = parser.parse_args(argv)

    if args.constants:
        _print_constants()
        return 0
    if args.ke:
        _compute_kinetic(args.ke[0], args.ke[1])
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
