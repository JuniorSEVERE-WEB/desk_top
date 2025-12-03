def convert(sentence: str)->str:
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence 

def main():
    text = input("Type your text: ")
    print(convert(text))

main()    

":)  🙂       :(  🙁"