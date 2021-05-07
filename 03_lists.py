myName = "Bé"
myAge = 41
mylist = "hello world !".title().split()

# print(mylist, type(mylist))
# print(myName, type(myName))

mylist.append("!!")
mylist.insert(0, "Attention")

print(mylist)

a=[1, 2, 3, 4]
a[a.index(3)]="5"
del a[1]

print(a.remove(1))
print(a)
