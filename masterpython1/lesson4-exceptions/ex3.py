class NegativeNumberError:
    pass 

def verify_number(num):
    if float(num) < 0:
        raise ValueError("Don't type a negative number")
    return float(num) 

def main():
    x = verify_number("Type a positive  number") 
    print(f"Tu as tape {x}")

main()    