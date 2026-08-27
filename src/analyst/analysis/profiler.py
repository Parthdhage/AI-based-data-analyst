import  pandas as pd
def profile_dataset(df: pd.DataFrame) -> dict:
    
    rows, columns = df.shape
    if(columns == 0):
        raise ValueError("No columns present")
    info = df.describe().to_dict()
    missing = df.isna().sum().to_dict()
    unique_values = df.nunique().to_dict()
    return{
        "rows": rows,
        "columns": columns,
        "stats": info,
        "missing": missing,
        "unique_values": unique_values}
