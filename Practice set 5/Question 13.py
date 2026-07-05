list1 = [1, 2, 3, 3, 4]
print("List of numbers contain duplicate elements ", list1)
temp = set(list1)
print("Converted list in set to remove duplicate elements ", temp)
list1 = list(temp)
print("Converted set in list ", list1)

