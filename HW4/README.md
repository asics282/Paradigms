## Урок 4. Функциональное программирование

```python
"""
Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).
Можете использовать любую парадигму, но рекомендую использовать функциональную, т.к.
в этом примере она значительно упростит вам жизнь.
"""

from random import randint
from math import sqrt


def random_array(array):
    for i in range(30):
        array.append(randint(1, 100))
    return array


def pearson(array_x, array_y):
    n = len(array1)
    sum_x = sum(array_x)
    sum_y = sum(array_y)
    sum_xy = sum(list(map(lambda x,y: x*y, array_x, array_y)))
    sum_xx = sum(list(map(lambda x: x*x, array_x)))
    sum_yy = sum(list(map(lambda y: y*y, array_y)))

    numerator = ((n*sum_xy)-(sum_x*sum_y))
    denumerator = sqrt(((n*sum_xx) - sum_x**2)*((n*sum_yy) - sum_y**2))
    return numerator/denumerator


array1 = []
array2 = []

x = random_array(array1)
y = random_array(array2)
print(x, y, sep="\n")

print(f'Корреляция Пирсона равна: {pearson(array1, array2)}')
```