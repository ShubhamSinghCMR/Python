class Banking:
    account_balance=0

    def __init__(self, in_bal):
        self.account_balance=in_bal

    def withdrawl(self, amount, file):
        if self.account_balance-amount >=0:
            self.account_balance=self.account_balance-amount
            file.write(f"Withdrawn - Rs {amount}. Account Balance: {self.account_balance} \n")
        else:
             print("Low account balance. Operation can't be performed.")

    def deposit(self, amount, file):
        self.account_balance=self.account_balance+amount
        file.write(f"Deposited - Rs {amount}. Account Balance: {self.account_balance} \n")

    @property
    def check_balance(self):
        return self.account_balance

try:
    in_bal=int(input("Enter initial balance in your account: "))
except Exception as e:
            print(f"Invalid amount: {e}")
else:
    obj=Banking(in_bal)

    try:
        file = open('transaction_detail.txt','w')
    except Exception as e:
                print(f"Error in opening file: {e}")

    while True:
        try:
            user_choice=int(input("\nSelect operation:\n1. Withdrawl\n2. Deposit\n3. Check balance\n4. Exit\nYour choice: "))
        except Exception as e:
            print(f"Incorrect choice: {e}")

        if user_choice == 1:
            try:
                amount=int(input("Enter amount: "))
            except Exception as e:
                print(f"Invalid amount: {e}")
            obj.withdrawl(amount,file)
        elif user_choice == 2:
            try:
                amount=int(input("Enter amount: "))
            except Exception as e:
                print(f"Invalid amount: {e}")
            obj.deposit(amount,file)
        elif user_choice == 3:
            print(f"Current balance: Rs {obj.check_balance}")
        elif user_choice == 4:
            print("Have a good day! Exiting...")
            break
        else:
            print("Enter correct choice...")

    file.close()