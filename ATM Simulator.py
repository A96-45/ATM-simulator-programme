name = input("Enter your name: ").upper()  # Convert the output to uppercase
print(f"Hello {name}, welcome to World Bank ATM simulator!")

# Initialize the account balance which will later be increased by deposit or decreased by withdrawing
Initial_balance = float(1000)

# Set and verify pin for the user
user_pin = 8888

# Allow user to enter the pin with a maximum of 3 attempts
attempts = 0
max_attempts = 3
atm_on = False

# Loop for PIN entry attempts
while attempts < max_attempts:
    entered_pin = int(input("Enter your PIN: "))

    if entered_pin == user_pin:
        print("Correct PIN!")
        atm_on = True  # Turn on the ATM if the PIN is correct
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempt(s) left.")

    if attempts == max_attempts:
        print("Too many incorrect attempts. Exiting the program.")
        atm_on = False
        break

# Now we enter the main ATM interface
# Use a while loop controlled by the atm_on flag
while atm_on:
    print("Main Menu")
    print("1. Deposit funds")
    print("2. Withdraw funds")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        deposit = float(input("Enter your deposit amount: "))
        print("__________________________")
        Initial_balance += deposit
        print(f"You have deposited Ksh.{deposit}")
        print(f"Your balance is Ksh.{Initial_balance}")
        print("__________________________")

    elif choice == "2":
        withdraw = float(input("Enter your withdraw amount: "))
        print("__________________________")
        if withdraw > Initial_balance:
            print("Insufficient funds!")
        else:
            Initial_balance -= withdraw
            print(f"You have withdrawn Ksh.{withdraw}")
        print(f"Your balance is Ksh.{Initial_balance}")
        print("__________________________")

    elif choice == "3":
        print(f"Your balance is Ksh.{Initial_balance}")
        print("__________________________")

    elif choice == "4":
        print("Thank you for using the ATM simulator!")
        print("Exiting ...........")
        atm_on = False
        break

    else:
        print("Invalid choice. Please enter a valid choice.")
