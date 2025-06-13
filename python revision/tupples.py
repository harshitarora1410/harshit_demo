mytupple = ("harshit",10.25, 2, 3, False)

print(mytupple[2])  # Accessing the third element
print(mytupple[1:4])  # Slicing from second to fourth element

x = list(mytupple)  # Converting tuple to list
x.append("spark iit")  # Appending a new element

x.remove(2)  # Removing the element with value 2
print(x)  # Printing the modified list

mytupple = tuple(x)  # Converting the list back to a tuple
print(mytupple)  # Printing the final tuple
print(type(mytupple))  # Checking the type of mytupple
