def replacement(sentence: str)->str:
    sentence = sentence.replace(" ", "...")
    return sentence 

def main():
    text = input("Type a text: ")
    print(replacement(text))

if __name__ == "__main__":
    main()
        