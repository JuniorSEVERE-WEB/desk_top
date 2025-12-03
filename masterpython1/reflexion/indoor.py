def convert(sentence:str)->str:
    sentence = sentence.lower().strip()
    return sentence 

def main():
    text = input("Type your text: ")
    print(convert(text))

if __name__ == "__main__":
    main()

