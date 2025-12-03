def convert(sentence):
    sentence = sentence.replace(":)", "🙂.")
    sentence = sentence.replace(":(", "🙁.")
    print(sentence)


def main():
    text = input("Type a text: ")
    convert(text)

main()    