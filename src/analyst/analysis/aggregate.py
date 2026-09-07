import pandas as pd

ALLOWED = {"sum", "max", "min", "mean", "std", "count"}
ALLOWED_FREQ = {"D", "W", "M", "Q", "Y"}
ALLOWED_DIRECTION = {"top", "bottom"}


def group_by(df, group_column, value_column, how):
    if group_column not in df.columns:
	    raise ValueError(f"Group column not found: {group_column}")
    if value_column not in df.columns:
	    raise ValueError(f"Value column not found: {value_column}")
    if how not in ALLOWED:
	    raise ValueError(f"Operation {how} not valid")

    result = getattr(df.groupby(group_column)[value_column], how)().to_dict()
    return result


def time_trend(df, date_column, value_column, how, freq) -> dict:
    if date_column not in df.columns:
	    raise ValueError(f"Date column not found: {date_column}")
    if value_column not in df.columns:
	    raise ValueError(f"Value column not found: {value_column}")
    if how not in ALLOWED:
	    raise ValueError(f"Operation {how} not valid")
    if freq not in ALLOWED_FREQ:
	    raise ValueError(f"Frequency {freq} not valid")

    df2 = df.copy()
    df2[date_column] = pd.to_datetime(df2[date_column])

    grouped = getattr(df2.groupby(df2[date_column].dt.to_period(freq))[value_column], how)().to_dict()

    dropped_rows = df2[date_column].isna().sum()
    dropped_value_sum = df2[df2[date_column].isna()][value_column].sum()

    return {
        "result": {str(k): float(v) for k, v in grouped.items()},
        "dropped_rows": int(dropped_rows),
        "dropped_value_sum": float(dropped_value_sum),
    }

def top_n(df, n, group_column, value_column, how, direction):
    if group_column not in df.columns:
	    raise ValueError(f"Group column not found: {group_column}")
    if value_column not in df.columns:
	    raise ValueError(f"Value column not found: {value_column}")
    if how not in ALLOWED:
	    raise ValueError(f"Operation {how} not valid")
    if direction not in ALLOWED_DIRECTION:
	    raise ValueError(f"Wrong Input Direction")
    if not isinstance(n, int) or n < 1:
	    raise ValueError(f"n must be a positive integer, got: {n}")
    grouped_result = getattr(df.groupby(group_column)[value_column], how)()
    if direction == "top":
	    top_sort = grouped_result.nlargest(n).to_dict()
    else:
	    top_sort = grouped_result.nsmallest(n).to_dict()
    return top_sort


	