

def drop_first_last(grades):
    """
    从任意长度的可迭代对象中分解元素
    :param grades: 成绩，可迭代对象
    :return:
    """
    first, *middle, last = grades
    return sum(middle)/len(middle)


if __name__ == '__main__':
    avg = drop_first_last((1, 2, 3, 4, 5, 6))
    print(*(avg, avg))
    record = ('ABCD', 50, 123.45, (12, 18, 2019))
    name, *_, (*_, year) = record
    print(*[name, year])