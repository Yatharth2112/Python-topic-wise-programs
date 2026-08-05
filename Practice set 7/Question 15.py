def even(a):
    return a%2 == 0

l = [10, 11, 12, 13, 14]
new1 = list(filter(even, l))
print(new1)