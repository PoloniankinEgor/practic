packets=input("введите последовательности успешно доставленных (1) и потерянных (0) пакетов данных. ")


if len(packets)<5:
    print("Длина строки должна быть не меньше 5")
elif not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    #  Общее количество пакетов
    all_packet=len(packets)
    #  Подсчёт количества потерянных пакетов (нулей)
    lost_packets=packets.count('0')

    max_loss_streak = 0  # максимальная длина серии потерь
    current_streak = 0  # текущая длина серии потерь

    for packet in packets:
        if packet == '0':   # если пакет потерян
            current_streak += 1  # увеличиваем длину текущей серии
            if current_streak > max_loss_streak:
                max_loss_streak = current_streak # обновляем максимум
        else:
            current_streak = 0     # сброс, если пакет доставлен
    # процент потерь
    percent = (lost_packets / all_packet)*100
    if percent<=1:
        print("Отличное качество")
    elif percent<=5:
        print("Хорошее качество")
    elif percent<=10:
        print("Удовлетворительное качество")
    elif percent<=20:
        print("плохое качество")
    elif percent>20:
        print("Критическое состояние сети")
    print(f"общее количество пакетов: {all_packet}")
    print(f"Колличество потерянных пакетов:{lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_loss_streak}")
    print(f"процент потерь: {round(percent,2)}")

