txt=input("Введите текст: ")
words=txt.split()
letters=''
for word in words:
    if word[0].isupper() and len(word)>=3:
        letters += word[0]

print(f"Аббревиатура: {letters}")