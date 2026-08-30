import pandas as pd
import pytest

from analyst.analysis.aggregate import group_by

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-01-02", None],
    "region": ["north", "south", "north"],
    "revenue": [100.5, 200.0, 150.25],
})

def test_returns_sum():
	result = group_by(df, "region", "revenue", "sum")
	assert result["north"] == 250.75
	assert result["south"] == 200.0

def test_raises_group_column():
    with pytest.raises(ValueError):
        group_by(df, "reion", "revenue", "sum")

def teste_raises_value_column():
    with pytest.raises(ValueError):
        group_by(df, "region", "reenue", "sum")

def test_raises_operation():
    with pytest.raises(ValueError):
        group_by(df, "region", "revenue", "describe")