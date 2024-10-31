
# ATM machine and it's functionality with Object Oriented Programming

class Atm:         # Here I am creating a class called Atm

    # This is a static Or the Class variable that is always outside of a constructor.
    __count = 0

    def __init__(self):     # Here I created a self function with a constructor 
        # Instanc variables that are inside the constructor.
        # Here I am defining the variables
        self.__pin = ""
        self.__balance = 0

        self.sno = Atm.__count
        Atm.__count = Atm.__count + 1

        self.menu()

    @staticmethod           # In the static method, we do not need to pass the object, so we don't use self.
    def get_count():
        return Atm.__count
    
    @staticmethod           # In the static method, we do not need to pass the object, so we don't use self.
    def set_count(new):
        if type(new) == int:
            Atm.__count = new
        else:
            print("Sorry! Not Allowed")
    
    def get_pin(self):
        return self.__pin
    

    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin changed successfully")
        else:
            print("Sorry! not allowed")



    def menu(self):

        # I am asking the user to selecting an option by giving an input
        user_input = input('''
                    Hello! How would you like to proceed:
                    1. Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    5. Enter 5 to exit
 ''')
        
        # The options will work depending on the user input
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Thank you! Bye for now.")
    

    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin set successfull")
        self.menu()

    def deposit(self):
        # write a code to check the type of the input if anything other than int then reject 
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the anount: "))
            self.__balance = self.__balance + amount
            print("Deposit Successfull")
        
        else:
            print("Sorry! Invalid Pin")
        self.menu()

    
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw Successfull")
            else:
                print("Sorry! Insufficient Balance")
        else:
            print("Sorry!, Invalid Pin")
        self.menu()

    

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Sorry! Invalid Pin.")
        
        self.menu()



atm = Atm()
