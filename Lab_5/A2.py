import re
text=input("введите текст: ")
sentences = re.split(r'(?<=[.?!]) ', text)
predl=0
for i in sentences:
    print(i)
    predl+=1
print("Предложений в тексте: ",predl)