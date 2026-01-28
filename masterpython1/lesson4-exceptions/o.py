def tab_add(n):
    for i in range(1, 11):
        print(f" {n} + {i} = {n + i}")

def tab_multi(n):
    for i in range(1, 11):
        print(f" {n} * {i} = {n * i}")  

def tab_minus(n):
    for i in range(1, 11):
        print(f" {n} - {i} = {n + i}")    

def tab_division(n):
    for i in range(1, 11):
        print(f" {n} / {i} = {n / i}")                  

def main():
    print("======Afficher une table du chiifre positif que vous entrer======")
    print("Type 1 for addition table")
    print("Type 2 for multiplication table ")
    print("Type 3 for minus table ")
    print("Type 1 for division table ")
    print("Type 5 for quit")


    while True:
        try:
            input_n = int(input("Type your number table: "))
        except ValueError:
            print("Oh no! Type a number")
            continue 

        try:
            choice = int(input("choose your type of table"))
        except ValueError:
            print("Oh no! Type a number!")   
            continue 

        if choice == 1:
            result = tab_add(input_n)
        elif choice == 2:
            result = tab_multi(input_n)  
        elif choice == 3:
            result = tab_minus(input_n)
        elif choice == 4:
            result = tab_division(input_n)  
        elif choice == 5:
            print("You quit the program!")
            return 
        else:
            print("You have to type a number between 1 and 5") 
            continue 
            

        



if __name__ == "__main__":
    main()    
