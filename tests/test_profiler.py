import pandas as pd
import pytest

from analyst.analysis.profiler import profile_dataset

def test_returns_corret_shape():
	df = pd.DataFrame({
	"Name":["Avinash", "Pranav", "Parth"],
	"Age":[20, 28, 21],
	})
	result = profile_dataset(df)
	assert result["rows"] == 3
	assert result["columns"] == 2

def test_counts_missing_value():
	df = pd.DataFrame({
	"name":[None, "Pranav", "Parth"],
	"age":[20, 28, 21],
	})
	result = profile_dataset(df)
	assert result["missing"]["name"] == 1
	assert result["missing"]["age"] == 0

def test_empty_dataframe_raises():
    with pytest.raises(ValueError):
        profile_dataset(pd.DataFrame())