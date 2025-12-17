def triangle_left(size):
    for i in range(size):
        for j in range(i + 1):
            print("#", end="")
        print()

def main():
    input_size = int(input("Type your size: "))
    affichage = triangle_left(input_size)
    print(affichage)

main()
