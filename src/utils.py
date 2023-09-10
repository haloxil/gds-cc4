"""
Common functions
"""
import numpy as np

def populate_empty_values(df):
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.fillna('NA')
    return df