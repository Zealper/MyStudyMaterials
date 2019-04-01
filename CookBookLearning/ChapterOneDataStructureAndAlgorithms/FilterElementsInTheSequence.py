import math
from itertools import compress

my_list = [1, -1, 3, 5, -10, 5, 9, 10, 35, -89]
print([n for n in my_list if n > 0])
print([n for n in my_list if n < 0])
pos = (n for n in my_list if n > 0)
print(pos)
for x in pos:
    print(x)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

# Outputs ['1', '2', '3', '4', '5']

other = [math.sqrt(n) for n in my_list if n > 0]
print(other)
clip_neg = [n if n > 0 else 0 for n in my_list]
clip_pos = [n if n < 0 else 0 for n in my_list]
print(clip_neg)
print(clip_pos)

address = ["5412 N CLARK", "5148 N CLARK", "5800 N CLARK", "2122 N CLARK",
           "5645 N CLARK", "1060 N CLARK", "4801 N CLARK", "1039 N CLARK"]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(address, more5)))
