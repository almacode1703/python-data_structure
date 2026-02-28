def convert_to_dict(data):
    student_dict = {}

    for record in data:
        key = record[0]
        value = record[1:]
        student_dict[key] = value

    return student_dict


students = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

print("\nOriginal List:")
print(students)

print("\nDictionary after conversion:")
print(convert_to_dict(students))