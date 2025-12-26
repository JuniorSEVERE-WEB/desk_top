def add(x, y):
    return x + y 

def multi(x, y):
    return x * y 

def minus(x, y):
    return x - y 

def div(x, y):
    if y == 0:
        return None 
    return x / y 

def main():
    print("=====CALCULATRICE====== \n Choose your operation")

    print("1-Type 1 for addition"
          "2-Type 2 for multiplication"
          "3-Type 3 for minus"
          "4-Type 4 for division"
          "5-Type 5 for quit")
    
    while True:
        choice = int(input("Make your choice in these operation: "))
        if choice == 5:
            print("You quit the program, Goodbye")
            return 
        
        if choice not in (1, 2, 3, 4):
            print("Type 1 or 2 or 3 or 4 or 5")
            continue 

        
            

        while True:
            try:
                a = int(input("Type a: "))
                b = int(input("Type b: "))
                break 
            except ValueError:
                print(" Type a integer")
                continue 

        if choice == 1:
            result = add(a, b)
        elif choice == 2:
            result == multi(a, b)
        elif choice == 3:
            result = minus(a, b)
        elif choice == 4:
            result = div(a, b)     

        print(f"Result : {result:.2f}")               

if __name__ == "__main__":
    main()

