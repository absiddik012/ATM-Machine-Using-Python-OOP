
# ATM Machine Simulation with Object-Oriented Programming (OOP)




## Introduction
This project simulates an ATM machine and its functionality using Python and Object-Oriented Programming (OOP) principles. The Atm class provides essential banking operations such as PIN creation, balance checking, deposit, and withdrawal in a user-friendly, command-line interface.


## Key Features

- **Create PIN:** Allows users to set a PIN for secure transactions.
- **Deposit Money:** Users can deposit funds by entering their PIN and desired amount.
- **Withdraw Money:** Users can withdraw funds after PIN verification and sufficient balance check.
- **Check Balance:** Users can view their current balance after verifying their PIN.
- **Exit:** Option to exit the program at any time.
## Code Structures

- class Atm: Main class encapsulating all functionalities of the ATM, using OOP principles.

### Attributes:
- __pin: Private attribute to store the user's PIN.
- __balance: Private attribute to store the account balance.
- __count: Static variable to keep track of ATM instances.


### Methods:
- __init__(): Constructor that initializes PIN and balance, increments ATM instance count, and displays the menu.
- menu(): Displays the menu options and directs the user to the selected operation.
- create_pin(): Allows the user to set their PIN.
- deposit(): Deposits money into the account after PIN verification.
- withdraw(): Withdraws money if sufficient balance is available and PIN is correct.
- check_balance(): Displays the account balance after PIN verification.


### Static Methods:
- get_count(): Returns the current count of ATM instances.
- set_count(): Sets a new count for ATM instances (for administrative purposes).
## Prerequisite

- Python 3.x installed on your system
## Usage

1. Run the program: The program displays a menu with options to create a PIN, deposit, withdraw, check balance, or exit.
2. Follow prompts: Enter your PIN and select the operation you want to perform.
3. Continue: Each operation will return you to the menu until you choose to exit.
## Example Prompts

Hello! How would you like to proceed:
1. Enter 1 to create pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check balance
5. Enter 5 to exit

## Project Highlights

- OOP Concepts: Demonstrates encapsulation, data hiding, and static methods.
- User Interaction: Simple and interactive user interface through the command line.
- Security: Basic PIN validation to enhance security for transactions.
## Authors

- [Abu Bakar Siddik](https://github.com/absiddik012)


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the [LICENSE.md](LICENSE.md) file for details.

