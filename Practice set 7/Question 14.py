def cube(x):
    return x * x * x

print(cube(2))
l = [1, 2, 3, 4, 6, 4, 3]
new1 = list(map(cube, l))
print(new1)

