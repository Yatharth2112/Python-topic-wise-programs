def sum(num):
    if num == 1:
        return 1

    return num%10 + sum(num//10)

n = int(input("Enter number: "))
print(sum(n))