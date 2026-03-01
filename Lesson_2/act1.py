# Empty Tuple
my_tuple = ()
print(my_tuple)

# Tuple with integers
my_tuple = (1,2,3)
print(my_tuple)

#tuple with mixed datatype
my_tuple = (my_tuple, 1,2,3, True)
print(my_tuple)

#nested tuple
my_tuple = ("mouse", [1,2,3],[4,5,6])
print(my_tuple)

#How to access tuple elements
print(my_tuple[0])
print(my_tuple[1])

#nested tuple & nested index
n_tuple = ("mouse", [1,2,3],[4,5,6])
print(n_tuple[0][3])
print(n_tuple[1][1])

# tuple slicing
print(n_tuple[1:2])

#iterating through tuple
for letter in (my_tuple):
    print(letter)

