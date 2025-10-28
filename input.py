class InputSystem:
    _instance = None  # Step 1: Class-level variable to hold the single instance

    def __new__(cls):
        # Step 2: Ensure only one instance is created
        if cls._instance is None:
            cls._instance = super(InputSystem, cls).__new__(cls)
            print("Input System Initialized!")
        return cls._instance

    # Step 3: Methods to get inputs
    def get_number_input(self, prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def get_operator_input(self, prompt):
        while True:
            op = input(prompt).strip()
            if op in ['+', '-', '*', '/']:
                return op
            else:
                print("Invalid operator! Please enter one of +, -, *, /.")


# Example usage (you can integrate this with the rest of the calculator)
if __name__ == "__main__":
    # Step 4: Get singleton instance
    input_system = InputSystem()

    num1 = input_system.get_number_input("Enter first number: ")
    operator = input_system.get_operator_input("Enter operator (+, -, *, /): ")
    num2 = input_system.get_number_input("Enter second number: ")

    print(f"You entered: {num1} {operator} {num2}")
