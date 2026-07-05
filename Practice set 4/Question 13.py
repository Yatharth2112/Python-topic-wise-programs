def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter number: "))
print("Fibonacci series: ")

for i in range(n):
    print(fibonacci(i),end = " ") 