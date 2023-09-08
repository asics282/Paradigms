while True:
    try:
        num = int(input('Введите число от 1 до 9: '))
        if num in range(1, 10):
            for i in range(1, num+1):
                print()
                for j in range(1, 10):
                    print(f'{i} x {j} = {j * i}')
            break
    except ValueError:
        print('Введите число!')