registeredUsers = {
        "Sidney": "sidneypass",
        "Carl": "carlpass",
        "Mike": "mikepass"
    }

registeredUserCash = {
    "Sidney": 10000,
    "Carl": 8000,
    "Mike": 8500
}

print("Welcome!")
print("\n".strip())
while True:
    print("Please make a selection.")
    print("1. Create a new account")
    print("2. Log in to an existing account")
    print("3. Cancel")
    choice1 = int(input())

    if choice1 == 1:
        newName = input("Enter your name: ")
        newPass = input("Enter your password: ")
        registeredUsers.update({newName: newPass})
        registeredUserCash.update({newName: 0})
        print("You have been registered successfully!")
        print("\n".strip())
        continue

    elif choice1 == 2:
        name = input("Enter your name: ")
        
        if name in registeredUsers:
            password = input("Enter your passsword: ")
            if password == registeredUsers[name] :
                print(f"Welcome {name}")
                while True:
                    print("\n".strip())
                    print("What would you like to do today? Please make a choice:")
                    print("\n".strip())
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Account Balance")
                    print("4. End")
                    
                    choice2 = int(input())

                    if choice2 == 1:
                        deposit = int(input("How much would you like to deposit? "))
                        registeredUserCash[name] += deposit
                        print(f"You have successfully deposited {deposit}.")
                        choice3 = input("Would you like to make another transaction? (y/n) ")

                    elif choice2 == 2:
                        withdraw = int(input("How much would you like to withdraw? "))
                        registeredUserCash[name] -= withdraw
                        print(f"You have successfully withdrawn {withdraw}.")
                        choice3 = input("Would you like to make another transaction? (y/n) ")

                    elif choice2 == 3:
                        print(f"You have {registeredUserCash[name]} in your account.")
                        choice3 = input("Would you like to make another transaction? (y/n) ")
                    
                    elif choice2 == 4:
                        print("Thank you for using this ATM.")
                        print("\n".strip())
                        break

                    else:
                        print("Invalid choice. Try again.")

                    if choice3 == 'n':
                        print("Thank you for using this ATM.")
                        print("\n".strip())
                        break

            else:
                print("Incorrect password. Try again.")
        else:
            print("Invalid user. Please try again.")

    elif choice1 == 3:
        print("Thank you for using this ATM. Have a nice day.")
        break
    else:
        print("Invalid choice: Please try again.")
