# Creating a dictionary using curly braces
my_dict = {"name": "Alice", "age": 30, "profession": "Engineer"}

# Creating a dictionary using the dict() constructor
another_dict = dict(name="Bob", age=25, profession="Doctor")

# Accessing values
name = my_dict["name"]
age = my_dict["age"]
print(name)  # Alice
print(age)   # 30


# Adding a new key-value pair
my_dict["city"] = "New York"
print(my_dict)  # {'name': 'Alice', 'age': 30, 'profession': 'Engineer', 'city': 'New York'}

# Updating an existing value
my_dict["age"] = 31
print(my_dict)  # {'name': 'Alice', 'age': 31, 'profession': 'Engineer', 'city': 'New York'}

# Removing a key-value pair using del
del my_dict["profession"]
print(my_dict)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Removing a key-value pair using pop()
age = my_dict.pop("age")
print(my_dict)  # {'name': 'Alice', 'city': 'New York'}
print(age)      # 31

my_dict = {"name": "Alice", "age": 30, "profession": "Engineer"}

# keys() method returns a view object that displays a list of all the keys in the dictionary
keys = my_dict.keys()
print(keys)  # dict_keys(['name', 'age', 'profession'])

# values() method returns a view object that displays a list of all the values in the dictionary
values = my_dict.values()
print(values)  # dict_values(['Alice', 30, 'Engineer'])



# items() method returns a view object that displays a list of dictionary's key-value tuple pairs
items = my_dict.items()
print(items)  # dict_items([('name', 'Alice'), ('age', 30), ('profession', 'Engineer')])

# get() method returns the value for the specified key if key is in dictionary
name = my_dict.get("name")
print(name)  # Alice

# update() method updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs
my_dict.update({"age": 31, "city": "New York"})
print(my_dict)  # {'name': 'Alice', 'age': 31, 'profession': 'Engineer', 'city': 'New York'}

# clear() method removes all items from the dictionary
my_dict.clear()
print(my_dict)  # {}

