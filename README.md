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

## Требования

- Python **3.9 или новее** с `pip` и модулем `venv`.
- Git для клонирования репозитория.
- Доступ к индексу пакетов Python для установки зависимостей и сборки.
- GNU Make нужен только для необязательных команд ниже.

На Debian/Ubuntu необходимые инструменты можно установить командой
`sudo apt update && sudo apt install git python3 python3-venv python3-pip`.
На macOS и Windows установите Python с [python.org](https://www.python.org/downloads/)
и [Git](https://git-scm.com/downloads). На Windows проверьте доступность команды `py`.

## Установка из исходников

Сначала клонируйте репозиторий и перейдите в его корень:

```bash
git clone https://github.com/myacc77788-dev/PhysEX.git
cd PhysEX
```

Создайте и активируйте отдельное окружение. Linux/macOS (bash/zsh):

```bash
python3 --version  # требуется 3.9+
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
py -3 --version  # требуется 3.9+
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

В `cmd.exe` вместо последней команды используйте `.venv\Scripts\activate.bat`.
Если PowerShell запрещает активацию, менять политику выполнения не обязательно:
используйте `.\.venv\Scripts\python.exe` вместо `python` в следующих командах,
а CLI запускайте через `.\.venv\Scripts\python.exe -m physex.cli`.

После активации все команды ниже выполняются из корня репозитория:

```bash
python -m pip install -e .
physex --ke 2.0 10.0
```

Ожидаемый результат: `Кинетическая энергия: 100 Дж`.
Установка редактируемая: изменения в `src/physex/` доступны без переустановки.
У библиотеки нет обязательных зависимостей времени выполнения.

## Тесты

В том же окружении установите дополнительные зависимости для тестирования:

```bash
python -m pip install -e ".[test]"
python -m pytest
```

Ожидаемый результат: **65 passed**. Без дополнения `[test]` пакет `pytest`
не устанавливается. Команда `python -m pip` использует тот же интерпретатор,
что и `python -m pytest`, и не требует системной установки пакетов через `sudo`.

## Сборка пакета (необязательно)

Для запуска библиотеки и тестов сборка архива не нужна. Для получения wheel
и исходного архива установите отдельный инструмент сборки:

```bash
python -m pip install build
python -m build
```

Результат: `dist/physex-0.1.0-py3-none-any.whl` и
`dist/physex-0.1.0.tar.gz`. Зависимости сборки (`setuptools>=77.0.3`)
устанавливаются автоматически в изолированное окружение.

## Команды Make (необязательно)

При наличии GNU Make и активного окружения:

```bash
make install  # установить пакет и зависимости тестов
make test     # запустить тесты
make run      # вывести константы
```

Без активации можно явно выбрать интерпретатор, например:
`make test PYTHON=.venv/bin/python`. На Windows без Make используйте
эквивалентные команды `python -m pip install -e ".[test]"`,
`python -m pytest` и `python -m physex.cli --constants`.

## Если установка не удалась

- `python3` или `py` не найден: установите Python 3.9+ и откройте новый терминал.
- Ошибка `ensurepip is not available` при создании окружения на Debian/Ubuntu:
  установите `python3-venv` (или пакет `python3.X-venv` для выбранной версии)
  и повторите создание окружения.
- `No module named pip`: проверьте, что выбран Python с `pip`; для установщика
  с python.org можно выполнить `python -m ensurepip --upgrade`.
- `No module named pytest` или `build`: выполните соответствующую команду
  установки из раздела «Тесты» или «Сборка пакета».
- `physex` не найден: активируйте окружение и повторите установку; альтернативно
  используйте `python -m physex.cli --ke 2.0 10.0`.
- Ошибка `externally-managed-environment`: используйте виртуальное окружение,
  а не системный `pip`; не отключайте защиту системного Python.

Результаты проверки инструкций: [аудит установки](docs/setup-audit.md).

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
