import pandas as pd

ALLOWED = {"sum", "max", "min", "mean", "std", "count"}
def group_by(df, group_column, value_column, how):
        if group_column not in  df.columns:
            raise ValueError(f"Group column not found: {group_column}")
        if value_column not in df.columns:
            raise ValueError(f"Value column not found: {value_column}")
        if how not in ALLOWED:
            raise ValueError(f"Operation {how} not valid")
        result = getattr(df.groupby(group_column)[value_column], how)().to_dict()
        return result
    