import os


def open_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def write_file(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)

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

def print_output_file(task_num):
    output_path = get_output_path(task_num)
    with open(output_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"Output:\n{content}")