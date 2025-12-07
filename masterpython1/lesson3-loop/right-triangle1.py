def triangle_right(size):
    for i in range(size):
        for j in range(size):
            
            if j < size - (i + 1):
                print(" ", end="")
            else:
                print("#", end="")    
        print()

def main():
    input_size = int(input("Type your positive number: "))
    triangle_right(input_size)

main()    