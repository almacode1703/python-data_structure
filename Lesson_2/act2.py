#Set
mySet = { 1,2,3,4,5,6,6,7,7,8,8,9}
print(mySet)

mySet2 = {100}
print(mySet2)

mySet2.add(200)
mySet2.add(1)
mySet2.add(2)
print(mySet2)

# Difference
print(mySet2 - mySet)
print(mySet2.symmetric_difference(mySet))


