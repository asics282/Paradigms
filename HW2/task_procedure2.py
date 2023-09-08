def multy_table(n): # получение таблицы умножения
    for i in range(1, n+1):
        print()
        for j in range(1, 10):
            print(f'{i} x {j} = {j * i}')
 
def main(): # запуск программы
    while True:
        try:
            num = int(input('Введите число от 1 до 9: '))
            if num in range(1, 10):
                multy_table(num)
                break
        except ValueError:
            print('Введите число!')

if __name__ == '__main__':
    main()