def triangle_right_rev(size):
    for i in range(size):                     # i = 0 → size-1
        for j in range(size):                 # j = 0 → size-1
            
            # Condition : espaces d'abord, puis les #
            if j < i:
                print(" ", end="")
            else:
                print("#", end="")
        
        print()  # saut de ligne
        

def main():
    input_size = int(input("Type your positive number: "))
    triangle_right_rev(input_size)

main()
