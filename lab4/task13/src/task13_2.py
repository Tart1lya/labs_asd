import tracemalloc
import time
# Запускаем таймер для измерения времени работы программы
t_start = time.perf_counter()

# Включаем отслеживание памяти
tracemalloc.start()
class Node:
    """
    Класс для узла связного списка.
    Каждый узел будет хранить значение и ссылку на следующий узел.
    """

    def __init__(self, value):
        self.value = value  # Значение в узле
        self.next = None  # Ссылка на следующий узел


class Queue:
    """
    Класс для очереди, реализованной на основе связного списка.
    """

    def __init__(self, max_size=None):
        self.front = None  # Указатель на начало очереди (первый элемент)
        self.rear = None  # Указатель на конец очереди (последний элемент)
        self.size = 0  # Текущий размер очереди
        self.max_size = max_size  # Максимальный размер очереди (None - неограниченная очередь)

    def is_empty(self):
        """
        Проверка на пустоту очереди.
        """
        return self.size == 0

    def is_full(self):
        """
        Проверка на переполнение очереди.
        Возвращает True, если очередь переполнена.
        """
        if self.max_size is None:
            return False  # Если max_size не задан, очередь не может переполниться
        return self.size == self.max_size

    def enqueue(self, value):
        """
        Добавление элемента в очередь (в конец очереди).
        Если очередь переполнена, выводится ошибка.
        """
        if self.is_full():
            raise OverflowError("Очередь переполнена. Невозможно добавить элемент.")

        new_node = Node(value)

        if self.is_empty():
            self.front = self.rear = new_node  # Если очередь пустая, новый узел будет и первым, и последним
        else:
            self.rear.next = new_node  # Добавляем новый элемент в конец
            self.rear = new_node  # Обновляем указатель на конец очереди

        self.size += 1  # Увеличиваем размер очереди

    def dequeue(self):
        """
        Удаление элемента из очереди (с начала очереди).
        Если очередь пуста, выводится ошибка.
        """
        if self.is_empty():
            raise IndexError("Очередь пуста. Невозможно удалить элемент.")

        dequeued_value = self.front.value  # Сохраняем значение, которое будем удалять
        self.front = self.front.next  # Сдвигаем указатель на начало очереди

        if self.front is None:  # Если после удаления очередь пуста, обновляем указатель на конец
            self.rear = None

        self.size -= 1  # Уменьшаем размер очереди
        return dequeued_value  # Возвращаем значение удалённого элемента

    def peek(self):
        """
        Возвращает элемент, который сейчас в начале очереди, но не удаляет его.
        Если очередь пуста, выводится ошибка.
        """
        if self.is_empty():
            raise IndexError("Очередь пуста. Нет элементов для просмотра.")
        return self.front.value

print("\nTask 13_2")
# Пример использования очереди
if __name__ == "__main__":
    queue = Queue(max_size=3)  # Создаём очередь с максимальным размером 3

    try:
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        print(f"Первый элемент в очереди: {queue.peek()}")  # Просмотр первого элемента (10)
        print(f"Удалён элемент: {queue.dequeue()}")  # Удаляем 10
        print(f"Первый элемент в очереди после удаления: {queue.peek()}")  # Просмотр первого элемента (20)

        queue.enqueue(40)  # Добавляем 40
        print(f"Первый элемент в очереди после добавления: {queue.peek()}")  # Просмотр первого элемента (20)

        queue.enqueue(50)  # Попытка добавить 50 в переполненную очередь
        # Выводим время работы программы
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        # Выводим количество памяти, затраченной на выполнение программы
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

        # Останавливаем отслеживание памяти
        tracemalloc.stop()
    except Exception as e:
        print(f"Ошибка: {e}")
        # Выводим время работы программы
        print("Время работы: %s секунд" % (time.perf_counter() - t_start))
        # Выводим количество памяти, затраченной на выполнение программы
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")

        # Останавливаем отслеживание памяти
        tracemalloc.stop()
