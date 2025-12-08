def triangle_left(size):

    result = ""

    
    for i in range(size):
        for j in range(i + 1):
            result += "#"
        result += "\n"
    return result    

def main():
    input_size = int(input("Type your positive number: "))
    affichage = triangle_left(input_size)
    print(affichage)

main()    
