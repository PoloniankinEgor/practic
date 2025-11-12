text=input("Введите текст")

def sentence(text):

    while '(' in text and ')' in text:
        left = text.find('(')
        right = text.find(')')
        text = text.replace(text[left:right + 1], '')
    return text
print(sentence(text))

