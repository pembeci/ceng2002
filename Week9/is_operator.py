
a = [1,2,3]
b = a  # b is a reference to a
# a.append(100)
# a = [2,4]
a = a + [100]
print(b)

arr1 = [1,2,3]
arr2 = [1,2,3]
arr3 = arr2

print(arr1 == arr2)  # T
print(arr1 == arr3)  # T
print(arr2 == arr3)  # T

print(arr1 is arr2) # F
print(arr1 is arr3) # F
print(arr2 is arr3) # T

arr4 = [1,2,3]
arr5 = arr4
print(arr4 is arr5)
arr4.append(100)
print(arr4 is arr5)
arr4 = arr4 + [100]
print(arr4 is arr5)