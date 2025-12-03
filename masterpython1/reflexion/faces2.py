def convert(sentence: str) -> str:
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

def main():
    text = input("Type a text: ")
    converted_text = convert(text)
    print(converted_text)

main()