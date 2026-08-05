def sum_all(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

print(sum_all(6,7,8,9))
