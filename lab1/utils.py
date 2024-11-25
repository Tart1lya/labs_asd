import os

def get_output_path(task_num):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Это lab1
    task_dir = f'task{task_num}'  # Формируем строку типа 'task1', 'task2' и т.д.

    # Путь к папке txtf внутри соответствующей папки задания
    txtf_dir = os.path.join(base_dir, task_dir, 'txtf')


    # Отладочный вывод
    print(f"task_dir: {task_dir}")
    print(f"txtf_dir: {txtf_dir}")

    return os.path.join(txtf_dir, "output.txt")

def delete_prev_values(task_num):
    output_path = get_output_path(task_num)
    print(f"Путь к output.txt: {output_path}")  # Отладочный вывод
    with open(output_path, 'w') as file:
        pass  # Очищаем файл

# Очищаем output.txt при каждом запуске


def open_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if len(lines) == 2:
            n = lines[0]
            if lines[1][0] in "ABCDEFGHIJKLMNOPQRSTUYXWZ":
                arr = [i for i in lines[1]]
            else:
                arr = list(map(int, lines[1].split()))
            return n, arr
        if len(lines) == 4:
            n1 = lines[0]
            n2 = lines[2]
            arr1 = list(map(int, lines[1].split()))
            arr2 = list(map(int, lines[3].split()))
            return n1, arr1, n2, arr2
        else:
            n = int(lines[0].strip())
            arr1 = []
            for i in range(1, n + 1):
                row = list(map(int, lines[i].strip().split()))
                arr1.append(row)
            arr2 = []
            for i in range(n + 1, 2 * n + 1):
                row = list(map(int, lines[i].strip().split()))
                arr2.append(row)
        return arr1, arr2

def write_file(arr, file_name, mode='w'):
    with open(file_name, mode) as file:
        if isinstance(arr, str):
            file.write(arr + "\n")
        elif isinstance(arr, list):
            if isinstance(arr[0], list):
                for r in arr:
                    file.write(" ".join(map(str, r)) + "\n")
            else:
                file.write(" ".join(map(str, arr)) + "\n")
