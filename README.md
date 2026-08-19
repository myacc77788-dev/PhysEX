# PhysEX

**PhysEX** — это библиотека на Python для физических расчётов в единицах СИ.
Проект создан «с нуля» и включает модули по основным разделам школьной и
вузовской физики: константы, размерные величины, кинематика, динамика,
энергия, термодинамика и электродинамика.

## Возможности

- **Физические константы** (CODATA 2018): скорость света, постоянная Планка,
  постоянная Больцмана, число Авогадро, гравитационная постоянная и др.
- **Размерные величины** — класс `Quantity` с арифметикой и контролем единиц.
- **Готовые формулы** в каждом разделе с проверкой на вводе (деление на ноль,
  отрицательные значения и т. п.).
- **Тесты** (`pytest`) для всех модулей.
- **CLI** `physex` для быстрых расчётов из терминала.

## Установка

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

Для запуска тестов:

```bash
pip install -e ".[test]"
pytest
```

## Быстрый старт

```python
import physex
from physex.kinematics import free_fall_time
from physex.energy import kinetic_energy
from physex.units import Quantity

# Время падения с высоты 100 м
t = free_fall_time(100.0)
print(f"Время падения: {t:.3f} с")

# Кинетическая энергия тела 2 кг со скоростью 10 м/с
print(f"E_k = {kinetic_energy(2.0, 10.0)} Дж")

# Размерные величины
v = Quantity(3.0, "м") / Quantity(2.0, "с")
print(v)   # 1.5 м/с
```

Из командной строки:

```bash
physex --constants
physex --ke 2.0 10.0
```

## Структура проекта

```
src/physex/
├── __init__.py        # публичное API пакета
├── constants.py       # фундаментальные константы
├── units.py           # размерные величины (Quantity)
├── kinematics.py      # кинематика
├── dynamics.py        # динамика
├── energy.py          # энергия, работа, мощность
├── thermodynamics.py  # термодинамика
├── electrodynamics.py # электродинамика
└── cli.py             # командная строка
tests/                 # тесты pytest
```

## Примеры формул

| Раздел          | Функция                                    | Формула                  |
|-----------------|--------------------------------------------|--------------------------|
| Кинематика      | `final_velocity(v0, a, t)`                 | v = v0 + a·t             |
| Кинематика      | `displacement(v0, t, a)`                   | s = v0·t + ½·a·t²        |
| Динамика        | `gravitational_force(m1, m2, r)`           | F = G·m1·m2/r²           |
| Энергия         | `kinetic_energy(m, v)`                     | E_k = ½·m·v²             |
| Термодинамика   | `ideal_gas_pressure(nu, T, V)`             | p = ν·R·T/V              |
| Электродинамика | `coulomb_force(q1, q2, r)`                 | F = k·q1·q2/r²           |

## Лицензия

[MIT](LICENSE) © 2026 myacc77788-dev
