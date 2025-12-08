def triangle_rt(size):

    result = ""

    for i in range(size):
        for j in range(i + 1):
            result += " " * (size - (i + 1)) + "#" * (i + 1)
        result += "\n"
    return result    
    

def main():
    input_size = int(input("Type your positive number: "))
    affichage = triangle_rt(input_size)
    print(affichage)

main()    