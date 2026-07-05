import random

user = 0
comp = 0
user_win = 0
comp_win = 0
    
def check(comp, user):
    global user_win , comp_win
    if comp == user:
        user_win += 0
        comp_win += 0
        print("It 's Draw")
    elif comp == 1:
        if user == 2:
            comp_win += 1
        elif user == 3:
            user_win += 1
    elif comp == 2:
        if user == 1:
            user_win += 1
        elif user == 3:
            comp_win += 1
    elif comp == 3:
        if user == 1:
            comp_win += 1
        elif user == 2:
            user_win += 1        
    else:
        print("Invalid Choice \nTry again")                         

def score():
     print(f"User = {user_win}")
     print(f"Computer = {comp_win}")

while(1):
 user = int(input("Enter 1 for snake \nEnter 2 for water \nEnter 3 for gun \nEnter 4 to exit \nEnter your choice: "))
 comp = random.randint(1,3)
 match user:
    case 1:
        check(comp, 1 )
        score()
    case 2:
        check(comp, 2)
        score()  
    case 3:
        check(comp, 3)
        score()
    case 4:
        break
    case _: 
        print("Invalid Choice")