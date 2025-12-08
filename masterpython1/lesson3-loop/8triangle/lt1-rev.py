def triangle_lt_rev(size):

    result = ""

    for i in range(size):
        for j in range(size - i):
            result += "#" 
        result += "\n"
    return result    


def main():
    input_size = int(input("Type your positive number:  "))
    affichage = triangle_lt_rev(input_size)
    print(affichage)

main()    