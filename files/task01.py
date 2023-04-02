"""Напишите функцию collatz с одним аргументом n. Функция должна возвращать
2-элементный кортеж:
– первый элемент – число k (1 ≤ k < n) такое, что у него самая длинная траектория
среди всех чисел в диапазоне [1, n);
– второй элемент – длина его траектории."""

#v1
"""def collatz(n):
    my_dict = {}
    for i in range(2, n + 1):
        item = i
        my_list = []
        while item != 1:
            if item % 2:
                item = 3 * item + 1
                my_list.append(item)
            else:
                item = item // 2
                my_list.append(item)
        my_dict[len(my_list)] = str(i)

    max_length = max(my_dict.keys())
    return int(my_dict[max_length]), max_length


def main():
    print(collatz(10))"""

def collatz(n):
    my_dict = {}
    for i in range(2, n + 1):
        item = i
        my_list = []
        while item != 1:
            if str(item) in my_dict.keys():
                my_list = my_list + my_dict[str(item)]
                break
            elif item % 2:
                item = 3 * item + 1
                my_list.append(item)
            else:
                item = item // 2
                my_list.append(item)
        my_dict[str(i)] = my_list
    new_dict = {int(len(values)) : int(key) for key, values in my_dict.items()}
    max_len = max(new_dict.keys())
    return new_dict[max_len], max_len


def main():
    print(collatz(5))
if __name__ == "__main__":
    main()
