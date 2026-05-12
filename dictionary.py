# Dictionaries are used to store data in key-value pair
my_cat = {
    'size': 'fat',
    'color': 'grey',
    'age': 4,
    'name': 'billu'
}

# Accessing values from the dictionary
print(my_cat['color'])

# Dictionaries have keys not indexes so, my_cat[0] will result in a keyerror
# Dictionaries are unordered
# Trying to access a key that doesn't exist in dictionary will result in a KeyError

# Three important dictionary methods
# 1. keys() -> return data type `dict_keys`
# 2. values() -> return data type `dict_values`
# 3. items() -> return data type `dict_items`
# These returned values aren't true list (can't be modified and can't use append)
# But can be used in for loops
print()
for v in my_cat.values():
    print(v)

print()
for i in my_cat.items():
    print(i)

# If we want to get an actual list from one of these methods, pass its list-like return value to the `list()` fucntion.
print(list(my_cat.values()))

# While you can use many values for keys, you cannot use a list or dictionary as the key in a dictionary.
# These data types are unhashable, if you need a list for a dictionary key, use a tuple instead.
print()
dog = {
    ('color', 'name'): ('brown', 'hero'),
    'age': 5
}
for k in dog.keys():
    print(k)
print()

# `get()` method: takes 2 arguments. 
# 1. the key of the value to retrieve
# 2. a fallback value to return if that key doesn't exist
print(dog.get('age', 'NOt found'))
print(dog.get('breed', 'NOt found'))
print()

# `setdefault()` method: takes 2 arguments.
# 1. key to check for.
# 2. value to set at that key if the key doesn't exist.
dog.setdefault('breed', 'doberman')
print(dog)
dog.setdefault('breed', 'husky')
print(dog)
print()

# Nested dictionaries
all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}
print(all_guests)