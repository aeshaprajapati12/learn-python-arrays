import array as arr
arrdata = arr.array("I",[20,10,99,88,36,56])
print("First value is : ",arrdata[1])
print("\n")

from array import *
arrdata = arr.array("h",[20,10,99,88,36,56,20])
print("First value is : ",arrdata[1])
print("\n")

from array import *
arrdata = arr.array("l",[20,10,99,88,36,56])
for i in arrdata:
    print(i)
print("\n")

from array import *
arrdata = arr.array("f",[20,10,99,88,36,56,20])
print(arrdata[1:3])
print(arrdata[1:])
print(arrdata[3:])
print(arrdata[:])
print("\n")

from array import *
arrdata = arr.array("h",[20,10,99,88,36,56,20])
arrdata[1] = 45
print(arrdata)
print("\n")

from array import *
arrdata1 = array("i",[20,10,99,88,36,56,20])
arrdata2 = array("i",[30,20,69,68,56,36,10])

arrdata = arrdata1 + arrdata2
print(arrdata)

print("\n")

import array as arr
arrdata = arr.array("I",[20,10,99,88,36,56])
arrdata.append(45)
print(" value is : ",arrdata)
print("\n")

import array as arr
arrdata = arr.array("I",[20,10,99,88,36,56,20])
a1 = arrdata.count(20)
print(" value is : ",a1)
print("\n")


from array import *
arrdata1 = array("i",[20,10,99,88,36,56,20])
arrdata2 = array("i",[30,20,69,68,56,36,10])

arrdata1.extend(arrdata2)
print(arrdata1)

import array as arr
arrdata = arr.array("I",[20,10,99,88,36,56,20])
a1 = arrdata.index(20)
print(" value is : ",a1)
print("\n")


import array as arr
arrdata = arr.array("I",[20,10,99,88,36,56])
arrdata.insert(1,15)
print(" value is : ",arrdata)
print("\n")

import array as arr
arrdata = arr.array("I",[20,10,99,88,36,56])
arrdata.pop(1)
print(" value is : ",arrdata)
print("\n")

import array as arr
arrdata = arr.array("I",[20,10,99,88,36,56,20])
arrdata.remove(20)
print(" value is : ",arrdata)
print("\n")

import array as arr
arrdata = arr.array("I",[20,10,99,88,36,56])
arrdata.reverse()
print(" value is : ",arrdata)
print("\n")

import array as arr
arrdata = arr.array("I",[20,10,99,88,36,56])
a = len(arrdata)
print(" value is : ",a)
print("\n")



import array as a1
arrdata = a1.array("i" ,[])

n = int(input("Enter num of elements :"))
for i in range(n):
    n1 = int(input("Enter value :"))
    arrdata.append(n1)
print(arrdata)
print(type(arrdata))