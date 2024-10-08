# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Adding elements
set1.add(6)
print(set1)
# Removing elements
set1.remove(2)
print(set1)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Set operations
union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)

difference = set1 - set2
print(difference)

symmetric_difference = set1 ^ set2
print(symmetric_difference)
# Methods
is_member = 3 in set1
print(is_member)

set_length = len(set1)
print(set_length)

set1.clear()
print(set1)


