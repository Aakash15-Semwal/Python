import pandas as pd

df = pd.read_csv('../Pandas/Dataset/winemag-data-130k-v2.csv', index_col=0)
print(df.head())

# Summary Functions
print(df.describe())
print(df.points.describe())
# This method generates a high-level summary of the attributes of the given column.
# It is type-aware, meaning that its output changes based on the data type of the input.
print(df.taster_name.describe())
# To get the mean
print(df.points.mean())
# To see a list of unique values in a column
print(df.taster_name.unique())
# To see the number of times each value appears in a column
print(df.taster_name.value_counts())

# Maps
# A map is used to replace each value in a column with another value.
mean = df.points.mean()
print(df.points.map(lambda p: p - mean))
# The function we pass to `map()` can be any function that takes a single value as an argument and returns a single value.
# `map()` returns a new Series where all the values have been transformed by the function.

# `apply()` - similar to `map()`, but it can be used to apply a function to a Series or DataFrame.
def remean_points(row):
    row.points = row.points - mean
    return row

df.apply(remean_points, axis='columns')

