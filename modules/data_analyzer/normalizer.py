import pandas as pd

def normalize_column(df, column):
    mean = df[column].mean()
    median = df[column].median()
    std = df[column].std()

    def score_value(x):
        if pd.isna(x) or x == 0:
            return 1
        elif x >= mean + std:
            return 10
        elif x >= mean:
            return 7 + ((x - mean) / std) * 3
        elif x >= median:
            return 4 + ((x - median) / (mean - median)) * 3
        else:
            return 1 + ((x - df[column].min()) / (median - df[column].min())) * 3

    return df[column].apply(score_value)
