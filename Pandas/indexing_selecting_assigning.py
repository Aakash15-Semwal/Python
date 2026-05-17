import pandas as pd

df = pd.read_csv("Pandas/Dataset/winemag-data-130k-v2.csv", index_col=0)

# Access different columns of the dataframe
print(df.country)
print(df['country'])
# The indexing operator `[]` is more versatile than the dot notation.
# As it can handle column names with spaces or special characters.

print()
# To get a specific value
print(df['country'][23])

# Indexing with pandas
# .iloc[] is used for integer-based indexing
# .loc[] is used for label-based indexing

# INTEGER BASED SELECTION
# To select the first row of data in a DataFrame
print(df.iloc[0])
# Both loc and iloca are row-first, column-second

print()
# To select the first column of data in a DataFrame
print(df.iloc[:, 0])
# To selct just the second and third entries
print(df.iloc[1:3, 0])
# We can also pass a list
# df.iloc[[0, 1, 2], 0]

print()
# LABEL BASED SELECTION
# To select the first row of data in a DataFrame
print(df.loc[0])

# To select specific entries in a DataFrame
print(df.loc[0, 'country'])

# ONE MAJOR DIFFERENCE BETWEEN ILOC AND LOC
# iloc takes slice of 0-based integers
# loc takes slice of labels
print(df.iloc[0:2, 0])
print(df.loc[0:2, 'country'])


print()
# MANIPULATING THE INDEX
# The set_index() method can be used to set the index of a DataFrame
print(df.set_index('title'))

print()
# Conditional Selection
print(df.country == "US")
# To get all the rows where the country is the US
print(df[df.country == "US"]) # or df.loc[df.country == "US"]

# We can use the `&` operator to bring 2 conditions together
print(df.loc[(df.country == 'Italy') & (df.points >= 90)])
# We can use the `|` operator to bring 2 conditions together
print(df.loc[(df.country == 'Italy') | (df.points >= 90)])

# `isin()` method can be used to select rows where the value in a column is in a list
print(df.loc[df.country.isin(['US', 'Italy'])])

# `isnull()` and `notnull()` methods can be used to check for missing values
print(df.isnull())
print(df.loc[df.price.notnull()])

print()
# Assigning values to a column
df.country = "US"
print(df.country)

# with an iterable of values
df['index_backwards'] = range(len(df), 0, -1)
print(df['index_backwards'])

# Assigning values to a subset of rows
df.loc[0:2, 'country'] = "Italy"
print(df.loc[0:2, 'country'])