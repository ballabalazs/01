mySet = {1, 2, 9}

print(mySet, type(mySet))

mySet.add(5)

print(mySet, type(mySet))

mySet.update([4,6,7])
print(mySet, type(mySet))

mySet.remove(5)
mySet2 = {3, 5, 7, 9, 8, 11}
print(mySet2, type(mySet2))
print("Union: ", mySet | mySet2)
print("Intersection: ", mySet & mySet2)
print("Diff: ", mySet - mySet2)