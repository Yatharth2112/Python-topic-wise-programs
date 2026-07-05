str1 = input("Enter a sentence to check is it palindrome or not: ")
str2 = str1[::-1]
if (str1 == str2):
    print("Palindrome")
else:
    print("Not Palindrome")
        
