def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return None  # on retourne None pour dire: impossible
    return a / b


def main():
    print("=== CALCULATOR ===")

    while True:
        print("\nChoose an operation:")
        print("1 - Addition (+)")
        print("2 - Subtraction (-)")
        print("3 - Multiplication (*)")
        print("4 - Division (/)")
        print("5 - Quit")

        choice = input("Your choice: ").strip()

        if choice == "5":
            print("Goodbye!")
            return  # STOP the main() function

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Try again.")
            continue  # return to the menu

        # Ask numbers (and keep asking until valid)
        while True:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Please type only numbers!")
                continue

        # Compute
        if choice == "1":
            result = add(a, b)
            print(f"Result: {a} + {b} = {result}")

        elif choice == "2":
            result = minus(a, b)
            print(f"Result: {a} - {b} = {result}")

        elif choice == "3":
            result = mult(a, b)
            print(f"Result: {a} * {b} = {result}")

        else:  # choice == "4"
            result = div(a, b)
            if result is None:
                print("Error: cannot divide by 0.")
            else:
                print(f"Result: {a} / {b} = {result}")


main()
