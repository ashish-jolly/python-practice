# DAY 36
# proram 1
user_balance = 1000
try:
    withdrawal_amount = int(input("how much you want to withdraw"))
    if withdrawal_amount > user_balance:
        print("insufficient fund")
    else:
        print(user_balance - withdrawal_amount)
except ValueError:
    print("invalid input")

# program 2
user_balance = 5000
try:
    choice = input("enter 1 to deposit, 2 to withdraw, 3 to check balance")
    if choice == "1":
        deposit = int(input("how much do you want to deposit"))
        print(user_balance + deposit)
    elif choice == "2":
        withdrawal_amount = int(input("how much do you want to withdraw"))
        if withdrawal_amount > user_balance:
            print("insufficient funds")
        else:
            print(user_balance - withdrawal_amount)
    elif choice == "3":
        print(user_balance)
    else:
        print("invalid input")
except ValueError:
    print("invalid input")

# program 3
try:
    score = int(input("enter your score"))
    if score < 0:
        print("invalid score")
    elif score > 100:
        print("invalid score")
    elif score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score < 60:
        print("F") 
except ValueError:
    print("invalid input, try again")

    

