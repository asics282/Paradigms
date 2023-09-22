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