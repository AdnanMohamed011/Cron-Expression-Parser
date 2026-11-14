# Cron Expression Parser

A command-line tool written in Python that parses and expands five-field cron expressions into their corresponding values.

This project was built to strengthen my understanding of Python, input validation, functions, command-line interfaces, and automated testing.

## Features

- Parses standard five-field cron expressions.
- Supports wildcards (`*`), individual values, ranges, lists, and step values.
- Validates field counts and allowed numeric ranges.
- Handles invalid expressions with helpful error messages.
- Displays expanded cron fields in a readable format.
- Includes automated tests using `pytest`.

## Cron Expression Format

A cron expression contains five fields:

```text
minute hour day_of_month month day_of_week
```

| Field | Allowed values |
|---|---|
| Minute | 0–59 |
| Hour | 0–23 |
| Day of month | 1–31 |
| Month | 1–12 |
| Day of week | 0–6 (Sunday = 0) |

## Supported Syntax

| Syntax | Meaning | Example |
|---|---|---|
| `*` | Every allowed value | `*` |
| `5` | A specific value | `5` |
| `1-5` | A range of values, inclusive | `1-5` |
| `*/10` | Every 10 values, starting at the field minimum | `*/10` |
| `5/10` | Starting at 5, then every 10 values | `5/10` |
| `1-20/5` | Every 5 values within a range | `1-20/5` |
| `1,3,5` | A list of specific values | `1,3,5` |

## Requirements

- Python 3
- pytest (for running tests)

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project directory:

```bash
cd CRON_EXPRESSION_PARSER_REBUILD
```

Install pytest:

```bash
python -m pip install pytest
```

## Usage

Run the parser from your terminal:

```bash
python main.py "*/15 8 * * 1-5"
```

Example output:

```text
minute        | [0, 15, 30, 45]
hour          | [8]
day_of_month  | [1, 2, 3, ..., 31]
month         | [1, 2, 3, ..., 12]
day_of_week   | [1, 2, 3, 4, 5]
```

The output shows the expanded values for each field.

## Running Tests

Run the complete test suite:

```bash
pytest -v
```

The test suite covers:

- Valid individual field expressions.
- Invalid field expressions.
- Valid complete cron expressions.
- Invalid complete cron expressions.
- Boundary values and step expressions.

**Current test result:** 44 tests passing.

## Project Structure

```text
CRON_EXPRESSION_PARSER_REBUILD/
│
├── main.py
├── test_main.py
└── README.md
```

- `main.py`: Contains the parsing logic, expression expansion, output formatting, and CLI.
- `test_main.py`: Contains automated tests written with pytest.
- `README.md`: Project documentation.

## Limitations

- Supports five-field cron expressions only.
- Does not support special cron characters such as `?`, `L`, `W`, or `#`.
- Does not validate calendar-specific combinations, such as whether February has a particular day.
- Day-of-week values use `0` for Sunday through `6` for Saturday.
- Day-of-month and day-of-week scheduling semantics are not evaluated; the parser expands their fields independently.

## What I Learned

Through this project, I practiced:

- Breaking a problem into smaller functions.
- Working with strings, lists, loops, and Python's `range()`.
- Validating user input and raising exceptions.
- Building command-line interfaces with `argparse`.
- Writing parameterized tests with `pytest`.
- Rebuilding a project from memory to strengthen independent problem-solving skills.

