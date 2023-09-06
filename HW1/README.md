## Введение и основные типы парадигм

Задача №1
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

Задача №2
Написать точно такую же процедуру, но в декларативном стиле

```python
# сортировка списка в порядке убывания в императивном стиле
def sort_list_imperative(numbers):
    for _ in range(0, len(numbers)-1):
        for i in range(0, len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers

# сортировка списка в порядке убывания в декларативном стиле
def sort_list_declarative(numbers):
    sort_numbers = sorted(numbers, reverse=True)
    return sort_numbers

def main():
    numbers = [2, 4, 3, 19, -5, 98]
    print(f"Исходный список: {numbers}")

    print(f"Cортировка в императивном стиле: {sort_list_imperative(numbers)}")
    print(f"Cортировка в декларативном стиле: {sort_list_declarative(numbers)}")

main()
```