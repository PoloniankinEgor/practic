x1= int(input("введите x1:"))
x2= int(input("введите x2:"))
y1= int(input("ведите  y1:"))
y2= int(input("введите y2:"))
if x1>0 and y1>0 and x2>0 and y2>0:
    print ('yes,I')
elif x1<0 and y1>0 and x2<0 and y2>0:
    print("Yes,II")
elif x1<0 and y<0 and x2<0 and y2<0:
    print("Yes,III")
elif x1>0 and y1<0 and x2>0 and y2<0:
    print ("Yes,IV")
else:
    print('no')
