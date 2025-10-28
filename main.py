from input import InputSystem

class Calculator:
    def calculate(self, num1, operator, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero!"
        else:
            return "Invalid operator!"


def main():
    # Initialize the calculator and input system
    calculator = Calculator()
    input_system = InputSystem()
    
    print("=== Basic Calculator ===")
    print("Supported operations: +, -, *, /")
    print("Type 'quit' when prompted for first number to exit\n")
    
    while True:
        try:
            # Get first number (with quit option)
            first_input = input("Enter first number (or 'quit' to exit): ").strip()
            if first_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            num1 = float(first_input)
            
            # Get operator and second number using InputSystem
            operator = input_system.get_operator_input("Enter operator (+, -, *, /): ")
            num2 = input_system.get_number_input("Enter second number: ")
            
            # Calculate result
            result = calculator.calculate(num1, operator, num2)
            
            # Display result
            print(f"Result: {num1} {operator} {num2} = {result}")
            print("-" * 30)
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

