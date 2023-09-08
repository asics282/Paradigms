![Programming-Paradigms](/HW2/Programming-Paradigms.png)
## Структурная и процедурная парадигмы

Задача:

На вход подается число n.
Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм.

**Вариант №1**

*Структурная реализация:*
```python
while True:
    try:
        num = int(input('Введите число от 1 до 9: '))
        if num in range(1, 10):
            for i in range(1, num+1):
                  print(f'{num} x {i} = {i * num}')
            break
    except ValueError:
         print('Введите число!')
```

*Процедурная реализация:*
```python
def multy_table(n): # получение таблицы умножения
    for i in range(1, n+1):
        print(f'{i} x {n} = {i * n}')


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
```

**Вариант №2**

*Структурная реализация:*
```python
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
```
*Процедурная реализация:*
```python
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
```
---
Подготовил студент Geek Brains - **Ивлев Павел**.