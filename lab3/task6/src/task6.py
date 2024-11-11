# Импортируем библиотеки для отслеживания памяти и времени выполнения программы
import tracemalloc
import time
from lab3.utils import open_file, write_file

# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()


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
    n_and_m_str, A, B = open_file("../txtf/input.txt")
    n = int(n_and_m_str[0])
    m = int(n_and_m_str[1])

    # Проверка корректности входных данных
    if (1 <= n, m <= 6000) and (all(0 <= i <= 40000 for i in A)) and all(0 <= i <= 40000 for i in B):
        C = generate_pairwise_array(A, B)
        C.sort()
        # Подсчёт суммы каждого десятого элемента
        result = sum(C[i] for i in range(0, len(C), 10))
        write_file(result, "../txtf/output.txt")
    else:
        # Выводим сообщение об ошибке, если данные некорректны
        print('Введите корректные данные')

    # Выводим время работы программы
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    # Выводим количество памяти, затраченной на выполнение программы
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()  # Останавливаем отслеживание памяти
