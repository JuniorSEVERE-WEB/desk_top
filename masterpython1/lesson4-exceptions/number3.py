while True:
    try:
        x = int(input("Type a positive number: "))
    except ValueError:
        print("Oh no, you have to type a ")
    else:
        break 
print(f" x is {x}")            
#rrrrrrr