def add(x, y):
    return x + y 

def multi(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return None
    return x / y

def minus(x, y):
    return x - y 

def main():
    print("=== CALCULATOR ===")
    

    

    while True:
        print("Choose one in these in number: \n1-Addition \n2-Multiplication \n3-Division \n4-Minus \n5-Quit")
        choice = input("Choose what operation you want to make: ").strip()
        if choice == "5":
            print("Goodbye!")
            return 
        
        if choice not in ("1", "2", "3", "4"):
            print("oh, sorry, you have to type 1 or 2 or 3 or 4 or 5")
            continue 

        while True:
            try:
                a = float(input("Type the first number: "))
                b = float(input("Type the second number: "))
                break

            except ValueError:
                print("Don't type a string or boolean")  
                continue 

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = multi(a, b)
        elif choice == "3":
            result = div(a, b)
            if result is None:
                print("Error: cannot divide by 0.")
                continue 
        else:
            result = minus(a, b)



        print(f"Result : {result}")         

if __name__ == "__main__":
    main()




              
