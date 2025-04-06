"""

Write a program to simulate a simple banking system. The program should:

1.Store the account numbers, account holders' names, and balances of 5 bank accounts in a list.
2.Allow users to deposit or withdraw money from their accounts.
3.Print the updated account information after each transaction.
4.Prevent users from withdrawing more money than their current balance.

"""

accounts_list = [{"account_number": 12345, "account_holder": "John Doe", "balance": 1000.0},
                 {"account_number": 67890, "account_holder": "Jane Doe", "balance": 500.0},
                 {"account_number": 34567, "account_holder": "Bob Smith", "balance": 2000.0},
                 {"account_number": 90123, "account_holder": "Alice Johnson", "balance": 1500.0},
                 {"account_number": 45678, "account_holder": "Mike Brown", "balance": 2500.0}]

account_number = int(input("please enter your account number: "))
print("1 = deposit ")
print("2 = withdraw ")
amount_user_wants_to_deposit_or_withdraw = int(input("Do you want to deposit or withdraw money:  "))

index = 0

def deposit_or_withdraw():

    if amount_user_wants_to_deposit_or_withdraw == 1:
        amount_deposit = float(input("How much do you want to deposit:  "))
        amount_deposit += accounts_list[index]["balance"]
        print("You new account balance is ", amount_deposit)

    elif amount_user_wants_to_deposit_or_withdraw == 2:
        amount_withdraw = float(input("How much do you want to withdraw:  "))
        amount_withdraw -= accounts_list[index]["balance"]
        print("You new account balance is ", amount_withdraw)

    else:
        print("Please enter a valid number")

if account_number == 12345:
    deposit_or_withdraw()
elif account_number == 67890:
    index += 1
    deposit_or_withdraw()
elif account_number == 34567:
    index += 2
    deposit_or_withdraw()
elif account_number == 90123:
    index += 3
    deposit_or_withdraw()
elif account_number == 45678:
    index += 4
    deposit_or_withdraw()
else:
    print("Please enter a valid account number")
