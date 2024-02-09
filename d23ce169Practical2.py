# (A) Create a list and apply methods (append, extend, remove, reverse), arrange created list in ascending and descending order.
List = [1,2,3,4]

List.append(10)
print("After appending 10:", List)

List.extend([20, 30, 40])
print("After extending with [20, 30, 40]:", List)

List.remove(3)
print("After removing 7:", List)

List.reverse()
print("After reversing:", List)

ascending_order = sorted(List)
print("Ascending Order:", ascending_order)

descending_order = sorted(List, reverse=True)
print("Descending Order:", descending_order)




# (B) List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]
# From above list get word “orange” and “Python” & repeat this list five times without using loops.
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]
RepeatedList = [List1] * 5

print("orange:",List1[-1][-1])
print('python:',List1[4][0])
print("Repeated List five times:", RepeatedList)



# C) Create a list and copy it using slice function
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]
print("Original List:", original_list)
print("Copied List:", copied_list)



# D) Create a tuple and apply different type of mathematical operation on it (Sum, Maximum, minimum etc.)
tuple = (1,2,3,4,5)
print("Tuple:", tuple)
print("Sum:", sum(tuple) )
print("Maximum:", max(tuple))
print("Minimum:", min(tuple))
