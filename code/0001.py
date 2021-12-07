def two_sum(target, array):
    for i, item in enumerate(array):
        for j, item_2 in enumerate(array[i:]):
            if target - item == item_2:
                return i, j


if __name__ == '__main__':
    res = two_sum(9, [2, 5, 7, 1])
    print(res)