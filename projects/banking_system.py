class banking_info_user:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
    def user_info(self):
        print(f"Name of the user is {self.name}. account_number is {self.account_number}")
    def get_balance(self):
        return self.__balance
    def deposit(self):
        deposit_process = input("enter your name\n")
        if deposit_process == self.name:
            deposit_process2 = int(input("enter your account number\n"))
            if deposit_process2 == self.account_number:
                deposit_process3 = int(input("how much do you want to deposit\n"))
                self.__balance += deposit_process3
                print("deposit succesful\n","balance amount: ", self.__balance)
    def withdraw(self):
        withdraw_process = input("enter your name\n")
        if withdraw_process == self.name:
            withdraw_process2 = int(input("enter your account number\n"))
            if withdraw_process2 == self.account_number:
                withdraw_process3 = int(input("how much do you want to withdraw"))
                if withdraw_process3 > self.__balance:
                    print("insufficient fund")
                else:
                    print("withdraw succesful\n", "balance amount: ", self.__balance - withdraw_process3, )
    def checking_balance(self):
        checking_balance_process = input("enter your name")
        if checking_balance_process == self.name:
            checking_balance_process2 = int(input("enter your account number"))
            if checking_balance_process2 == self.account_number:
                print(self.__balance)
user1 = banking_info_user("Ashish", 1234, 5000)
user1.user_info()
print(user1.get_balance())
user1.deposit()
user1.withdraw()
user1.checking_balance()
class banking_info_user2(banking_info_user):
    pass
    def user_info(self):
        print(f"user name is {self.name}. account number given is {self.account_number}")
user2 = banking_info_user2("Shibi", 12345, 10000)
user2.user_info()
print(user2.get_balance())
user2.deposit()
user2.withdraw()
user2.checking_balance()