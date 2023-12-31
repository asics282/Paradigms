## Урок 6. Парадигмы программирования на практике. Подведение итогов курса

*Контекст*

Предположим, что мы хотим найти элемент в массиве (получить его индекс). Мы можем это сделать просто перебрав все элементы.
Но что, если массив уже отсортирован? В этом случае можно использовать бинарный поиск. Принцип прост: сначала берём элемент находящийся посередине и сравниваем с тем, который мы хотим найти. Если центральный элемент больше нашего, рассматриваем массив слева от центрального, а если больше - справа и повторяем так до тех пор, пока не найдем наш элемент.

*Задача*

Написать программу на любом языке в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

*Решение*
```python
'''
Бинарная сортировка
'''

array = [3, 5, 7, 18, 27, 38, 40, 100]

search_num = int(input('Введите искомое число: '))

def bin_search(array, search_num):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle = array[middle_index]

        if search_num == middle:
            return middle_index
        elif search_num < middle:
            right = middle_index - 1
        else:
            left = middle_index + 1

    return -1

result = bin_search(array, search_num)

if result != -1:
    print(f"Число {search_num} найдено в массиве, индекс: {result}")
else:
    print(f"Число {search_num} не найдено в массиве.")
```