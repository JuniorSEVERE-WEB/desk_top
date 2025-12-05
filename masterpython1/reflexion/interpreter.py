def convert(expression):
    # Ajouter des espaces autour des opérateurs
    for op in "+-*/":
        expression = expression.replace(op, f" {op} ")

    x, y, z = expression.split()

    x = float(x)
    z = float(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z    
    elif y == "*":
        result = x * z 
    elif y == "/":
        if z == 0:
            print("error")
            exit()
        result = x / z

    return result


def main():
    text = input("Type your calc here: ")
    converted = convert(text)
    print(f"{converted:.2f}")


main()
