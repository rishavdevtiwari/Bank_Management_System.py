current_balance = 10000
transaction_history = [] #Initialized as an empty list
#append() is used to append data to the list transaction_history
print("Welcome to the ATM!")
username = input("Enter your username (Demo user: abc): ")#authentication prototype for username
if username != "abc":
    print("Invalid username, try using the demo account 'abc'")
else:
    password = input("Enter your password (Demo password: 123): ")#authentication prototype for password
    if password != "123":
        print("Invalid password, try using the demo password '123'")
    else:
        while True:
            print("\n1. Balance Inquiry") #Displays balance amt using f string
            print("2. Withdraw Cash") #withdrawal deducted from blance, stored in transaction history
            print("3. Deposit Cash") #deposit amount added to balance, stored in transaction history
            print("4. View Transaction History") #all transaction history retrieved from the list 'transaction_history'
            print("5. Exit") #either terminate program or continue program
            choice = input("Please enter your choice (1-5): ")

            if choice == '1':
                print(f"Your current balance is {current_balance}")
            elif choice == '2':
                amount = int(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                else:
                    if amount > current_balance:
                        print("Insufficient balance.")
                    else:
                        current_balance -= amount
                        transaction_history.append(f"Withdrawn: {amount}")
                        #Stores the data passed as argument from append()
                        print(f"Withdrawn amount: {amount}")
                        print(f"Remaining balance: {current_balance}")
            elif choice == '3':
                amount = int(input("Enter the amount to deposit: "))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                else:
                    current_balance += amount
                    transaction_history.append(f"Deposited: {amount}")
                    #stores the argument passed in append() into transaction_history
                    print(f"Deposited amount: {amount}")
                    print(f"New balance: {current_balance}")
            elif choice == '4':
                print("Transaction History:")
                for transaction in transaction_history:
                #the for loop iterates over each item
                #printing every item
                #the history is stores in 'transaction'
                    print(transaction)
            elif choice == '5':
                confirm_exit = input("Are you sure you want to exit? (yes/no): ")
                if confirm_exit.lower() == 'yes':
                    print("Thank you for using our services!")
                    break
                else:
                    continue
            else:
                print("Invalid choice. Please try again.")
                
#'transaction_history' is a list in this program to store strings that represent each transaction
#The program will continue to run until the user chooses to exit. When the user chooses to exit
#the program will print a message thanking the user for using the program and then terminate.
#'transaction_history' stores all data during runtime, deletes everything after program is terminated.