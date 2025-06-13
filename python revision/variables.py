age = 21
Age = 22
AGE = 22

print(age, Age, AGE)

name1 = "harshit"
name2 = "dhruv"
name3 = "varun"

print(name1, name2, name3)

marks1 = 7.8
marks2 = 8.0
marks3 = 8.2

print(marks1, marks2, marks3)

print(type(marks1))
print(type(name2))
print(type(age))

#             [0,    1,    2, 3,  4]
mylist = ["harshit",10.25, 2, 3, False]
print(mylist)
print(mylist[-1])
print(mylist[1:4])

mylist.append("spark iit")
print(mylist)

mylist.reverse()
print(mylist)

mylist.insert(2, "inserted value")
print(mylist)

mylist[4] = "changed value"
print(mylist)

mylist.remove("changed value")
print(mylist)

mylist.pop(2)
print(mylist)

mylist.sort()
print(mylist)