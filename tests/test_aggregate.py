import pandas as pd
import pytest

from analyst.analysis.aggregate import group_by
from analyst.analysis.aggregate import time_trend
from analyst.analysis.aggregate import top_n

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-01-02", None],
    "region": ["north", "south", "north"],
    "revenue": [100.5, 200.0, 150.25],
})
#checking group_by function
def test_returns_sum():
	result = group_by(df, "region", "revenue", "sum")
	assert result["north"] == 250.75
	assert result["south"] == 200.0

def test_raises_group_column():
    with pytest.raises(ValueError):
        group_by(df, "reion", "revenue", "sum")

def test_raises_value_column():
    with pytest.raises(ValueError):
        group_by(df, "region", "reenue", "sum")

def test_raises_operation():
    with pytest.raises(ValueError):
        group_by(df, "region", "revenue", "describe")

#checking time_trend function

def test_returns_normal():
    result = time_trend(df, "date", "revenue", "sum", "M")
    assert result["result"]["2024-01"] == 300.5

def test_returns_dropped_value_sum():
    result = time_trend(df, "date", "revenue", "sum", "M")
    assert result["dropped_value_sum"] == 150.25

def test_returns_dropped_rows():
    result = time_trend(df, "date", "revenue", "sum", "M")
    assert result["dropped_rows"] == 1

def test_bad_freq():
    with pytest.raises(ValueError):
        time_trend(df, "date", "revenue", "sum", "K")

def test_bad_column():
    with pytest.raises(ValueError):
        time_trend(df, "date", "reenue", "sum", "M")

#checking top_n function

def test_returns_top_n():
    n = 1
    result = top_n(df, n, "region", "revenue", "sum", "top")
    assert result["north"] == 250.75

def test_bad_direction():
    n = 1
    with pytest.raises(ValueError):
        top_n(df, n, "region", "revenue", "sum", "side")


def test_bad_n():
    n = 1
    with pytest.raises(ValueError):
        top_n(df, "abc", "region", "revenue", "sum", "top")