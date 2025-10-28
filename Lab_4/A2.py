n=int(input("введите значение n"))
m=int(input("введите значение m"))
print("Прямоугольник", n,'x',m)
for i in range(n):  # Внешний цикл - строки
     for j in range(m):  # Внутренний цикл – столбцы
      print(' # ', end='')
     print()
print("\n")
print("Правый треугольник")
for i in range(1,n+1):  # Внешний цикл - строки

    print(' # '*i, end='')
    print()
print("\nРамка", n, 'x', m)
for i in range(n):
    for j in range(m):
        # если первая/последняя строка или первый/последний столбец
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()


