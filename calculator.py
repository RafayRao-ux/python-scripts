while True:
    try:
        operator = input("\nEnter an Operator ( +, -, *, /, ) or 'q' to quit: ")

        if operator == 'q':
            print("Goodbye!")
            break

        if operator not in ('+', '-', '*', '/'):
            print(f"{operator} is not a valid operator. Use +, -, *, /")
            continue  

        num1 = float(input("Enter Number 1: "))
        num2 = float(input("Enter Number 2: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = num1 / num2

        print(f"Result: {round(result, 3)}")

    except ValueError:
        print("Error: Please enter a valid number!")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break