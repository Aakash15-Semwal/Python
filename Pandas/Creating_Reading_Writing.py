import pandas as pd # To use pandas

# Creating data
# There are two main methods to create data in pandas:
# 1. Series (1-D data)
# 2. DataFrame (2-D data)

# DataFrame
print(pd.DataFrame({'Yes': [1,2], 'No': [3,4]}))
# DataFrame entries are not limited to integers
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}))
"""
We are using the pd.DataFrame() constructor.
When we pass a Python dict to the constructor, the keys of the dict are used as the column names, and the values of the dict are used as the data in the columns.

The list of row labels used in a DataFrame is known as an Index.
We can assign values to it by using an `index` parameter in our constructor
"""
print()
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B']))


# Series
print(pd.Series([1,2,3,4,5]))
print(pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A'))

print()
# Reading data files
# We can read the `csv` files by using pd.read_csv() function
wine_reviews = pd.read_csv("Pandas/Dataset/winemag-data-130k-v2.csv")
# We can use the `shape` attribute to get the number of rows and columns
print(wine_reviews.shape)
# We can use the `head()` method to get the first few rows
print(wine_reviews.head())
# To specify which column to use as index use `index_col` parameter
wine_reviews = pd.read_csv("Pandas/Dataset/winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.head())