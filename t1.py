from array import *
arr = array("i",[])

for i in range(5):
    num = int(input("enter number :"))
    arr.append(num)

for i in range(len(arr)):
     for j in range(len(arr)-1):
         if arr[j] > arr[j+1]:
             temp = arr[j]
             arr[j] = arr[j+1]
             arr[j+1] = temp

print("Ascending order :")
for i in arr:
    print(i,end=" ")
    for i in range(len(arr)):
     for j in range(len(arr)-1):
         if arr[j] < arr[j+1]:
             temp = arr[j]
             arr[j] = arr[j+1]
             arr[j+1] = temp

print("\n")
print("Descending order :")
for i in arr:
    print(i,end=" ")
    