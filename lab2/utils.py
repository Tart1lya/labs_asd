import os
def get_output_path(task_num):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Это lab1
    task_dir = f'task{task_num}'  # Формируем строку типа 'task1', 'task2' и т.д.

    # Путь к папке txtf внутри соответствующей папки задания
    txtf_dir = os.path.join(base_dir, task_dir, 'txtf')

    return os.path.join(txtf_dir, "output.txt")

def delete_prev_values(task_num):
    output_path = get_output_path(task_num)
    with open(output_path, 'w') as file:
        pass  # Очищаем файл


def open_file(file_name):
    with (open(file_name, 'r') as file):
        lines = [line.strip() for line in file if line.strip()]
        if len(lines) >= 2:
            data_n = list(map(int, lines[0].split()))
            n, arr_n = data_n[0], data_n[1:]
            data_k = list(map(int, lines[1].split()))
            k = data_k[0]
            arr_k = data_k[1:] if len(data_k) > 1 else []
            return [n] + arr_n, [k] + arr_k  # Возвращаем n, a и k, b



def write_file(arr, file_name, mode = 'w'):
    with open(file_name, mode) as file:
        if isinstance(arr, (str, int)):
            file.write(str(arr))
        elif isinstance(arr, list):
            if len(arr) > 0 and isinstance(arr[0], list):
                for r in arr:
                    file.write(" ".join(map(str, r)) + "\n")
            else:
                file.write(" ".join(map(str, arr)) + "\n")