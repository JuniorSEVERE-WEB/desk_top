def convert(sentence: str)-> str:
    return sentence.replace(":)", "🙂").replace(":(", "🙁")

def main():
    text = input("Type a text: ")
    print(convert(text))

if __name__ == "__main__":
    main()