# Задача 6: Очередь с приоритетами

## Описание

Данный код обрабатывает операции с приоритетной очередью, включая добавление, извлечение минимального элемента и уменьшение значений, записывает результаты операций `X` в `output.txt`, а также измеряет время выполнения и затраты памяти программы.
- Входные данные находятся в файле input.txt.
- В первой строке входного файла содержится число n (1 ≤ n ≤ 10^6) - число операций с очередью. Следующие n строк содержат описание операций с очередью, по одному
описанию в строке.

### Формат выходных данных
- Выводится последовательно результат выполнения всех операций X, по одному в каждой строке выходного
файла. Если перед очередной операцией X очередь пуста, вместо
числа выводится звездочка «*».

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab5/
|--   task6/
|     |-- src/
|     |     |-- task6.py      # Реализация алгоритма
|     |-- tests/
|     |     |-- test_task6.py       # Тесты
|     |-- txtf/
|     |     |-- input.txt     # Входные данные
|     |     |-- output.txt    # Выходные данные
```
## Код задачи
```
# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import time
import tracemalloc
from lab5.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Текущая директория
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Путь к директории с файлами
input_path = os.path.join(txtf_dir, "input.txt")


# Основная функция обработки операций
def process_priority_queue(operations):
    import heapq

    heap = []  # Минимальная куча
    element_map = {}  # Словарь для отслеживания актуальных значений
    id_map = {}  # Словарь: идентификатор строки → элемент
    removed = set()  # Множество удаленных элементов
    result = []  # Для хранения выходных данных

    current_id = 0  # Уникальный идентификатор для операций A

    for i, operation in enumerate(operations):
        parts = operation.split()
        if parts[0] == "A":
            # Добавляем элемент в кучу
            x = int(parts[1])
            heapq.heappush(heap, (x, current_id))
            element_map[current_id] = x
            id_map[i + 1] = current_id  # i+1 соответствует строке x + 1
            current_id += 1

        elif parts[0] == "X":
            # Удаляем минимальный элемент
            while heap and heap[0][1] in removed:
                heapq.heappop(heap)  # Пропускаем удаленные элементы

            if heap:
                _, element_id = heapq.heappop(heap)
                result.append(str(element_map[element_id]))
                removed.add(element_id)
            else:
                result.append("*")

        elif parts[0] == "D":
            # Уменьшаем значение элемента
            x = int(parts[1]) + 1
            y = int(parts[2])
            element_id = id_map[x]  # Получаем идентификатор элемента

            # Уменьшаем значение в словаре
            element_map[element_id] = y

            # Добавляем в кучу новое значение
            heapq.heappush(heap, (y, element_id))

    return result


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    lines = open_file(input_path)
    n = int(lines[0])  # Число операций
    operations = lines[1:]  # Список операций

    # Проверка корректности входных данных
    if 1 <= n <= 10 ** 6 and all(len(op.split()) in (1, 2, 3) for op in operations):
        print(f"\nTask: 6\nInput:\n{n}\n{operations}\n")
        delete_prev_values(6)  # Очищаем предыдущие результаты

        # Обрабатываем операции
        results = process_priority_queue(operations)

        output_path = get_output_path(6)
        # Записываем результаты операций X в файл output.txt
        write_file("\n".join(results), output_path)
        print_output_file(6)
    else:
        print("Введите корректные данные")

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()

```
## Запуск проекта

1. Перейдите в директорию task6.
2. Перейдите в директорию txtf.
3. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
4. Вернитесь в директорию task6.
5. Перейдите в директорию src.
6. Запустите скрипт:
      python task6.py
   
7. Результат выполнения будет записан в файл output.txt в директории txtf.

## Пример

### Входные данные (input.txt)
```
8
A 3
A 4
A 2
X
D 2 1
X
X
X
```


### Выходные данные (output.txt)
```
2
3
4
*
```
