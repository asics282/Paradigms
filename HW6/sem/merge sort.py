'''
Сортировка слиянием
'''

array = [3, 100, 27, 18, 7, 38, 40]

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        middle = len(array)//2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
