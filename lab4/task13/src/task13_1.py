import tracemalloc
import time


t_start = time.perf_counter()
tracemalloc.start()

class Node:
    """Класс для создания узлов связного списка."""
    def __init__(self, data):
        self.data = data  # Данные, которые хранит узел
        self.next = None  # Ссылка на следующий узел (изначально None)

class Stack:
    """Класс для стека на основе связного списка."""
    def __init__(self):
        self.top = None  # В стеке нет элементов, top указывает на None

    def isEmpty(self):
        """Проверка, пуст ли стек."""
        return self.top is None  # Если top равен None, стек пуст

    def push(self, data):
        """Добавление элемента в стек."""
        new_node = Node(data)  # Создаем новый узел с переданными данными
        new_node.next = self.top  # Новый узел указывает на текущий top
        self.top = new_node  # Теперь новый узел стал верхом стека

    def pop(self):
        """Удаление элемента из стека."""
        if self.isEmpty():
            print("Стек пуст. Невозможно удалить элемент.")
            return None  # Если стек пуст, возвращаем None
        popped_node = self.top  # Сохраняем верхний узел
        self.top = self.top.next  # Теперь top указывает на следующий узел
        return popped_node.data  # Возвращаем данные удаленного элемента

    def print_stack(self):
        """Вывод элементов стека."""
        current = self.top  # Начинаем с верхнего элемента
        if self.isEmpty():
            print("Стек пуст.")
        else:
            while current:  # Пока текущий элемент не равен None
                print(current.data, end=" -> ")  # Выводим данные текущего узла
                current = current.next  # Переходим к следующему элементу
            print("None")  # Конец стека

print("\nTask 13_1")
if __name__ == "__main__":
    # Пример использования стека
    stack = Stack()  # Создаем пустой стек
    stack.push(10)  # Добавляем элемент 10
    stack.push(20)  # Добавляем элемент 20
    stack.push(30)  # Добавляем элемент 30

    print("Стек после добавления элементов:")
    stack.print_stack()  # Выводим стек

    print("\nУдаленный элемент:", stack.pop())  # Удаляем верхний элемент (30)
    print("Стек после удаления элемента:")
    stack.print_stack()  # Выводим стек после удаления элемента

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
