# a = [12,5,7,84,8,6,4,11,10]
# print(type(a))



# for i in a:
#     print(i)  # Iterating through the list



# s = "harshit"
# for i in s:
#     print(i)  # Iterating through the string



n = 1
while n <= 10:
    print(n)  
    n += 1
    if n == 3:
        continue
    # Skipping the iteration when n is 3
    if n == 8:
        break  # Exiting the loop when n is 5

print("  ")  



def rec (n):
    if n == 10:
        return
    elif n <= 10:
        print(n)
    rec(n + 1)

rec(1)  # Calling the recursive function starting from 1
