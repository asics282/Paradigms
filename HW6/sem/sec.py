'''
Программа секундомер
'''
import time

start_time = time.time()

button = input("Введите команду: ")
try:
    while True:
        if button == "Старт":
            elapsed_time = time.time() - start_time
            print(f"Прошло времени: {round(elapsed_time, 2)}", end="\r")
except KeyboardInterrupt:
    print()
    print(f'Стоп: {round(elapsed_time, 2)}')