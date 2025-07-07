# a set is a collection of unique elements
# it is unordered and unindexed 
# sets are mutable, but the elements must be immutable
# a set is used when you want to store unique items and do not care about the order

set1 = {"apple", "banana", "cherry",12,4556,48, 12.5, "apple"}
print(type(set1))

print(set1)  # Output: {'banana', 'cherry', 'apple', 12, 4556, 48, 12.5}

for i in set1:
    print(i)  # Iterating through the set

set1.add("orange")  # Adding an element to the set
print(set1)  # Output: {'banana', 'cherry', 'apple', 12, 4556, 48, 12.5, 'orange'}  

set1.remove("banana")  # Removing an element from the set
print(set1)  # Output: {'cherry', 'apple', 12, 4556, 48, 12.5, 'orange'}
# if the element is not present, remove raises an error

set1.discard("apple")  # Discarding an element from the set
print(set1)  # Output: {'cherry', 12, 4556, 48, 12.5, 'orange'}
# if the element is not present, discard does not raise an error

set2 = {1,2,3,4,5,True}

set1.update(set2)
print(set1)  # Output: {'cherry', 1, 2, 3, 4, 5, 12, 4556, 48, 12.5, 'orange'}