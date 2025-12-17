#1-function main()
   #1.0-ask if add, mult, div, minus
   #1.1-enter a value
   #1.3-give you the table you want

def table_add(n):
    for i in range(11):
        print(f"{n} + {i} = {n + i}")
    
def table_mult(n):
    for i in range(11):
        print(f"{n} * {i} = {n * i}")   

def table_minus(n):
    for i in range(11):
        print(f"{n} - {i} = {n - i}")
    
def table_div(n):
    for i in range(11):
        print(f"{n} / {i} = {n / i}")
    


def main():
    ask = int(input("Type your positive number: "))

    choice = input("" \
    "choose your table by a numero" \
    "               1-Add" \
    "               2-Minus" \
    "               3-div" \
    "               4-multi:   ")

    if choice == "1":
        table_add(ask)
    elif choice == "2":
        table_minus(ask)  
    elif choice == "3":
        table_div(ask)
    elif choice == "4":
        table_mult(ask)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()        

              


        