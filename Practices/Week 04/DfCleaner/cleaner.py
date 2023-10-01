import pandas as pd

df = df.dropna()
df
df.mean()
df['salary'].fillna(121605.05, inplace=True)
df['bonus'].fillna(7.66, inplace=True)

df.reset_index

df['employed_date'] = pd.to_datetime(df['employed_date'])
    return df