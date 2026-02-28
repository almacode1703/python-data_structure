my_dict = {}

# dict with integer keys
my_dict = { 1: 'apple', 2:'orange'}

# dict with mixed keys
my_dict = {
    'name' : "John",
    1:[2,3,4]
}

# Output
print(f"Name : {my_dict['name']}")
print(f"Name : {my_dict.get('name')}")

#Update value
my_dict['age'] = 27
print(f"Age : {my_dict['age']}")
print(f"Age : {my_dict.get('age')}")

#Address
my_dict['address'] = "Downtown,Chicago"
print(f"My Address : {my_dict.get('address')}")

#Remove particular element
my_dict.pop('age')
print(my_dict)


#remove all the elements
my_dict.clear()
print(my_dict)