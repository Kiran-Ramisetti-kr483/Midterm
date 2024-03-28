import sys
from app.commands import Command
from app.plugins.addition import AdditionCommand
from app.plugins.subtraction import SubtractionCommand
from app.plugins.multiplication import MultiplicationCommand
from app.plugins.division import DivisionCommand

class MenuCommand(Command):
    def execute(self, args):
        print("Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("You chose Addition")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = AdditionCommand().execute([num1, num2])  # Call execute method of AdditionCommand
            
        elif choice == "2":
            print("You chose Subtraction")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = SubtractionCommand().execute([num1, num2])  # Call execute method of SubtractionCommand
            
        elif choice == "3":
            print("You chose Multiplication")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = MultiplicationCommand().execute([num1, num2])  # Call execute method of MultiplicationCommand
           
        elif choice == "4":
            print("You chose Division")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = DivisionCommand().execute([num1, num2])  # Call execute method of DivisionCommand
            
        elif choice == "5":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid option.")
