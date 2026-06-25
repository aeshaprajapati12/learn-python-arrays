from array import *

arr = array("i", [])

for i in range(5):
    num = int(input("Enter number: "))
    arr.append(num)

max_num = arr[0]

for i in arr:
    if i > max_num:
        max_num = i

print("Maximum number:", max_num)


print("\n")

from array import *

arr = array("i", [])

for i in range(5):
    num = int(input("Enter number: "))
    arr.append(num)

# Sort in ascending order
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted Array:")
for i in arr:
    print(i, end=" ")

print("\nMaximum number:", arr[len(arr) - 1])

print("\n")

from array import *

arr = array("i", [])

for i in range(5):
    num = int(input("Enter number: "))
    arr.append(num)

min_num = arr[0]

for i in arr:
    if i < min_num:
        min_num = i

print("Minimum number:", min_num)


print("\n")

from array import *

arr = array("i", [])

for i in range(5):
    num = int(input("Enter number: "))
    arr.append(num)

# Sort in ascending order
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] < arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted Array:")
for i in arr:
    print(i, end=" ")

print("\nMinimum number:", arr[len(arr) - 1])

print("\n")



