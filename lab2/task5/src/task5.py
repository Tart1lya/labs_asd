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
