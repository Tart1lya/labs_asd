# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
from lab3.utils import *

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория task1/src
txtf_dir = os.path.join(os.path.dirname(current_dir), "txtf")  # Директория task1/txtf
input_path = os.path.join(txtf_dir, "input.txt")
# Генерация массива попарных произведений
def generate_pairwise_array(A, B):
    C = []
    for a in A:
        for b in B:
            C.append(a * b)
    return C


# Основной блок программы
if __name__ == "__main__":
    # Читаем данные из файла input.txt с помощью функции open_file
    n_and_m_str, A, B = open_file(input_path)
    n = int(n_and_m_str[0])
    m = int(n_and_m_str[1])

    # Проверка корректности входных данных
    if (1 <= n, m <= 6000) and (all(0 <= i <= 40000 for i in A)) and all(0 <= i <= 40000 for i in B):
        delete_prev_values(6)
        C = generate_pairwise_array(A, B)
        C.sort()
        # Подсчёт суммы каждого десятого элемента
        result = sum(C[i] for i in range(0, len(C), 10))
        output_path = get_output_path(6)
        write_file(result, output_path)
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()  # Останавливаем отслеживание памяти
