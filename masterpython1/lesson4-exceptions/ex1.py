x = float(input("Enter x: "))

y = float(input("Enter y: "))

try:
    print(f"x/y give {x / y}")
except ZeroDivisionError:
    print("Don't type 0 at y")




