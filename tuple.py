my_tuple = (1, 2, 3)
print(my_tuple)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)
print(combined_tuple)

repeated_tuple = tuple1 * 3  # (1, 2, 3, 1, 2, 3)
print(repeated_tuple)

sliced_tuple = combined_tuple[1:4]  # (2, 3, 4)
print(sliced_tuple)

my_tuple = (1, 2, 2, 2, 3)
count = my_tuple.count(2)  # 2
print(count)


# Creating a tuple
person = ("Alice", 30, "Engineer")

# Accessing elements
name = person[0]
age = person[1]
profession = person[2]

# Concatenation
person_with_address = person + ("New York",)

# Repetition
doubled_person = person * 2

# Slicing
slice_of_person = person[1:3]

# Using tuple methods
occurrences_of_30 = person.count(30)
index_of_engineer = person.index("Engineer")

# Printing results
print(name)  # Alice
print(age)  # 30
print(profession)  # Engineer
print(person_with_address)  # ("Alice", 30, "Engineer", "New York")
print(doubled_person)  # ("Alice", 30, "Engineer", "Alice", 30, "Engineer")
print(slice_of_person)  # (30, "Engineer")
print(occurrences_of_30)  # 1
print(index_of_engineer)  # 2
