# Задача 5: Представитель большинства

## Описание

Код проверяет, содержится ли во входной последовательности элемент, который встречается больше половины раз, используя метод "Разделяй и властвуй"
### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит число n (1 ≤ n ≤ 10^5) — количество элементов в массиве.
- Вторая строка содержит n целых чисел, по модулю не превосходящих 10^9.


### Формат выходных данных
- В выходном файле output.txt должен содержаться 1, если во входной последовательности есть элемент, который встречается строго больше половины раз, в противном случае - 0.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab2/
|--   task5/
|     |-- src/
|     |     |-- task5.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task5.py       # Тесты
|     |-- txtf/
|     |     |-- input.txt     # Входные данные
|     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
import tracemalloc
import time
from lab2.utils import open_file, write_file
t_start = time.perf_counter()
tracemalloc.start()

def count_occurrences(arr, num, left, right):

    count = 0
    for i in range(left, right):
        if arr[i] == num:
            count += 1
    return count

def majority_element_rec(arr, left, right):

    if left == right - 1:
        return arr[left]


    mid = (left + right) // 2
    left_majority = majority_element_rec(arr, left, mid)
    right_majority = majority_element_rec(arr, mid, right)


    if left_majority == right_majority:
        return left_majority


    left_count = count_occurrences(arr, left_majority, left, right)
    right_count = count_occurrences(arr, right_majority, left, right)


    if left_count > (right - left) // 2:
        return left_majority
    elif right_count > (right - left) // 2:
        return right_majority
    else:
        return None

if __name__ == "__main__":
    n_list, arr = open_file("../txtf/input.txt")

    n = int(n_list[0])


    if 1 <= n <= 10**5 and (all(abs(i) <= 10**9 for i in arr)):
        write_file("", "../txtf/output.txt", mode="w")

        majority_element = majority_element_rec(arr, 0, n)
        if majority_element is not None:
            if count_occurrences(arr, majority_element, 0, n) > n // 2:
                write_file('1\n', "../txtf/output.txt", mode="a")
            else:
                write_file('0\n', "../txtf/output.txt", mode="a")
        else:
            write_file('0\n', "../txtf/output.txt", mode="a")
    else:
        print('Введите корректные данные')

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()








```
## Запуск проекта

1. Перейдите в директорию task5.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task5.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task5.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
5
2 3 9 2 2

### Выходные данные (output.txt)
1
