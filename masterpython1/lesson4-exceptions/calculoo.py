#def add,multi v
#def main
   #input choisir chiff add(while True)
   #input to enter a and b(while true)
   #if chosir == 1( result = add )
def add(x, y):
    return x + y 

def minus(x, y):
    return x - y 

def multi(x, y):
    return x - y 

def div(x, y):
    if y == 0:
        return None 
    return x / y 
   


def main():
    print("=====CALCULATRICE====")
    print("Type 1 for add")
    print("Type 2 for minus")
    print("Type 3 for multi")
    print("Type 4 fpr division")
    print("Type 5 for quit")
    while True:
        try:
            choice = int(input("choose your operation by a number between 1 and 5:"))
        except ValueError:
            print("oh no! don't type a string")
            continue

        if choice == 5:
            print("Goodbye! You close the program.")
            return 
        
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Choose between 1 and 5.")
            continue 


        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: ")) 
            

        except ValueError:
            print("oh no! Don't type a string") 
            continue  

        if choice == 1:
            result = add(a, b)
        elif choice == 2:
            result = minus(a, b)        
        elif choice == 3:
            result = multi(a, b)
        elif choice == 4:
            result = div(a, b)
            if result is None:
                print("Error: cannot divide by 0.")
                continue   
        print(f"Result : {result:.2f}")             

    

if __name__ == "__main__":
    main()    