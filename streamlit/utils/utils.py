import pandas as pd

def anonymize_columns(df, columns_with_prefix):
    """
    Anonymizes specified columns in a DataFrame with consistent mappings and custom prefixes.
    
    Args:
        df (pd.DataFrame): The DataFrame to anonymize.
        columns_with_prefix (dict): Dictionary with column names as keys and prefixes as values.

    Returns:
        pd.DataFrame: Anonymized DataFrame.
        dict: Mapping dictionary {column_name: {original_value: anonymized_value}}.
    """
    df = df.copy()
    mappings = {}

    for col, prefix in columns_with_prefix.items():
        unique_vals = df[col].dropna().unique()
        value_map = {val: f"{prefix}-{i+1}" for i, val in enumerate(sorted(unique_vals))}
        df[col] = df[col].map(value_map)
        mappings[col] = value_map

    return df, mappings
