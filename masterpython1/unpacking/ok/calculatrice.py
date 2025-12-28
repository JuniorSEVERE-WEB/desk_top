def add(x, y):
    return x + y 

def minus(x, y):
    return x - y 

def multi(x, y):
    return x * y 

def div(x, y):
    return x / y 



def main():
    print("1-Type 1 for addition \n2-Type 2 for minus \n3-Type 3 for multiplication  \n4-Type 4 for division \n5-Type 5 for quit")
    choice = int(input("make your choice: "))
    while True:
        if choice == 1:
            add(a, b)
        elif choice == 2:
            minus(a, b)
        elif choice == 3:
            multi(a, b)
        elif choice == 4:
            div(a, b)
        elif choice == 5:
            print("You quit the program, Goodbye")
            return
        
        ############
            


if __name__ == "__main__":
    main()    