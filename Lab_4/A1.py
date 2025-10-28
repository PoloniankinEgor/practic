import random
import time
N=int(input('введите количество примеров: '))
own_time = time.time()     # общее время начала работы программы
correct_count=0             # количество правильных ответов
total_time = 0             # суммарное время на все примеры
for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    while True:
        try:
            start_time = time.time()  # текущее время
            answer = int(input(f"{a} × {b} = "))  # ввод пользователя
            time_spent = (time.time() - start_time ) # время, затраченное на решение
            total_time += time_spent  # добавляем к суммарному времени
            if a*b==answer:
                correct_count += 1
                print(f"Верно! (Время: {round(time_spent,1)} сек)")
            else:
                print(f"неверно! Правильно:{a*b} (Время: {round(time_spent,1)} сек)")
            break

        except ValueError:  # отлавливаем ошибку ввода
            print("Пожалуйста, введите целое число")
end_time = time.time() - own_time
percent_correct =  round(correct_count / N * 100,1)
average_time = round(total_time / N, 1)
# ======= СТАТИСТИКА =======
print("=" * 50)
print("СТАТИСТИКА:")
print("=" * 50)

print(f"Общее время: {round(end_time, 1)} секунд")
print(f"Среднее время на вопрос: {average_time} сек")
print(f"Правильных ответов: {correct_count}/{N}")
print(f"Процент правильных: {percent_correct}%")
