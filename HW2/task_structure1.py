while True:
    try:
        num = int(input('Введите число от 1 до 9: '))
        if num in range(1, 10):
            for i in range(1, num+1):
                  print(f'{num} x {i} = {i * num}')
            break
    except ValueError:
         print('Введите число!')