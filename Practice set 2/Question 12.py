n = int(input("Enter a number: ")) 
reversed_n = 0
while n > 0:
    last_digit = n % 10
    reversed_n = (reversed_n * 10) + last_digit
    n = n // 10

print("Reversed number:", reversed_n)