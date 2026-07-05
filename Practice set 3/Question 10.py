sentence = "Coding in Python is fun"
vowels = ['a', 'e', 'i', 'o', 'u']
sum = 0
for char in sentence.lower():
    if(char in vowels):
        sum = sum + 1

print(f"There are {sum} vowels in this sentence")        

