import pytest
from main import parse_field, expand_cron

@pytest.mark.parametrize("field_str, min_val, max_val, expected", [
    ("0", 0, 59, [0]),
    ("15", 0, 59, [15]),
    ("*", 0, 59, list(range(0, 60))),
    ("1-5", 0, 59, [1, 2, 3, 4, 5]),
    ("1,3,5", 0, 59, [1, 3, 5]),
    ("*/10", 0, 59, [0, 10, 20, 30, 40, 50]),
    ("2/10", 0, 59, [2, 12, 22, 32, 42, 52]),
    ("5-15/2", 0, 59, [5, 7, 9, 11, 13, 15]),
    ("10-12", 0, 59, [10, 11, 12]),
    ("0,15,30,45", 0, 59, [0, 15, 30, 45])
])
def test_parse_field(field_str, min_val, max_val, expected):
    assert parse_field(field_str, min_val, max_val) == expected


@pytest.mark.parametrize("field_str, min_val, max_val", [
    ("60", 0, 59),
    ("-1", 0, 59),
    ("abc", 0, 59),
    ("1.5", 0, 59),
    ("5-", 0, 59),
    ("10-5", 0, 59),
    ("*/0", 0, 59),
    ("*/", 0, 59),
    ("1,,3", 0, 59),
    ("*/2/3", 0, 59)
])
def test_invalid_parse_field(field_str, min_val, max_val):
    with pytest.raises(ValueError):
        assert parse_field(field_str, min_val, max_val)


@pytest.mark.parametrize("cron_string, expected", [
    (
    "0 9 * * *",
    {
        "minute": [0],
        "hour": [9],
        "day_of_month": list(range(1, 32)),
        "month": list(range(1, 13)),
        "day_of_week": list(range(0, 7))
    }
),
(
    "30 18 * * *",
    {
        "minute": [30],
        "hour": [18],
        "day_of_month": list(range(1, 32)),
        "month": list(range(1, 13)),
        "day_of_week": list(range(0, 7))
    }
),
(
    "*/5 * * * *",
    {
        "minute": list(range(0, 60, 5)),
        "hour": list(range(0, 24)),
        "day_of_month": list(range(1, 32)),
        "month": list(range(1, 13)),
        "day_of_week": list(range(0, 7))
    }
),
(
    "0 */2 * * *",
    {
        "minute": [0],
        "hour": list(range(0, 24, 2)),
        "day_of_month": list(range(1, 32)),
        "month": list(range(1, 13)),
        "day_of_week": list(range(0, 7))
    }
),
(
    "0 8 * * 1-5",
    {
        "minute": [0],
        "hour": [8],
        "day_of_month": list(range(1, 32)),
        "month": list(range(1, 13)),
        "day_of_week": [1, 2, 3, 4, 5]
    }
),
(
    "15 10 1 * *",
    {
        "minute": [15],
        "hour": [10],
        "day_of_month": [1],
        "month": list(range(1, 13)),
        "day_of_week": list(range(0, 7))
    }
),
(
    "0 0 1 1 *",
    {
        "minute": [0],
        "hour": [0],
        "day_of_month": [1],
        "month": [1],
        "day_of_week": list(range(0, 7))
    }
),
(
    "0 12 * * 0",
    {
        "minute": [0],
        "hour": [12],
        "day_of_month": list(range(1, 32)),
        "month": list(range(1, 13)),
        "day_of_week": [0]
    }
),
(
    "0,30 8-18 * * 1-5",
    {
        "minute": [0, 30],
        "hour": list(range(8, 19)),
        "day_of_month": list(range(1, 32)),
        "month": list(range(1, 13)),
        "day_of_week": [1, 2, 3, 4, 5]
    }
),
(
    "5-25/5 * * * *",
    {
        "minute": [5, 10, 15, 20, 25],
        "hour": list(range(0, 24)),
        "day_of_month": list(range(1, 32)),
        "month": list(range(1, 13)),
        "day_of_week": list(range(0, 7))
    }
)
])
def test_expand_cron(cron_string, expected):
    assert expand_cron(cron_string) == expected


@pytest.mark.parametrize("cron_strngs", [
    "* * *",          # Only 3 fields
    "60 * * * *",     # Minute out of range
    "* 24 * * *",     # Hour out of range
    "* * 32 * *",     # Day of month out of range
    "* * * 13 *",     # Month out of range
    "* * * * 8",      # Day of week out of range (if max is 7)
    "a * * * *",      # Invalid character
    "*/0 * * * *",    # Zero step
    "10-5 * * * *",   # Reversed range
    "* * * * * *",    # 6 fields instead of 5
])
def test_invalid_expand_cron(cron_strngs):
    with pytest.raises(ValueError):
        assert expand_cron(cron_strngs)