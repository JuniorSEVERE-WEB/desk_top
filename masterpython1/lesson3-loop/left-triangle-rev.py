def triangle_rev(size):
    for i in range(size):
        for j in range(size - i):
            print("#", end="")
        print()

def main():
    input_size = int(input("Type your positive: "))
    affichage = triangle_rev(input_size)
    print(affichage)

main()    