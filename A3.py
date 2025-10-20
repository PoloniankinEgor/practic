
prev= int(input("введите предыдущие показания"))
new=int(input("Введите текущие показания"))
if new>=prev:
    result=new-prev
else:
    result=10000-prev+new
if result<= 300:
    bill=21
elif result<=600:
    bill= 21+(result-300)*0.06
elif result<=800:
    bill=21+300*0.06 + (result-600)*0.04
else:
    bill=21+300*0.06+200*0.04+(result-800)*0.025
avg=bill/result
print("предыдущее",prev)
print("текущее",new)
print("использовано",result)
print("к оплате",round(bill,2))
print("Ср цена m^3",round(avg,2))