def triangle_left_rev(size):
    result = ""

    for i in range(size):
        result += "#" * (size - i) + "\n"
    return result     

def main():
    input_size = int(input("Type your positive number: "))
    affichage = triangle_left_rev(input_size)
    print(affichage)

main()    