x1=int(input("x1 "))
y1=int(input("y1 "))
x2=int(input("x2 "))
y2=int(input("y2 "))
color1=(x1+y1)%2 # 0 - белая, 1 - чёрная
color2=(x2+y2)%2 # 0 - белая, 1 - чёрная
if color1==color2:
    print ("Yes")
    if color1==0 :
        print('White')
    else:
        print('Black')
else:
    print("No")