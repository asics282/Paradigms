## Урок 5. Логическое программирование

Написать программу на языке Prolog для вычисления суммы
элементов списка. На вход подаётся целочисленный массив.
На выходе - сумма элементов массива.

```prolog
% Правило для вычисления суммы элементов списка
sum_list([], 0). % Сумма пустого списка равна 0
sum_list([Head|Tail], Sum) :- 
    sum_list(Tail, TailSum), % Рекурсивный вызов для хвоста списка
    Sum is Head + TailSum.   % Сумма равна голове списка плюс сумме хвоста

% Пример использования:
% Вызов sum_list([1, 2, 3, 4, 5], X) вернет X = 15.
```