# 2.
# Given a list lst and a number N,
# create a new list that contains each number of lst at most N times without reordering.
# For example if N = 2, and the input is [1,2,3,1,2,1,2,3],
# you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times,
# and then take 3, which leads to [1,2,3,1,2,3]
import timeit

# def delete_nth(order, max_e):
#     # code here
#     start = timeit.default_timer()
#     for i in order:
#         i_number = order.count(i)
#         if i_number > max_e:
#             j = i_number - max_e
#             order.reverse()
#             for n in range(j):
#                 order.remove(i)
#             order.reverse()
#     end = timeit.default_timer()
#     print(end-start)
#     return order


def delete_nth(order,max_e):
    start = timeit.default_timer()
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    end = timeit.default_timer()
    print(end - start)
    return ans


if __name__ == '__main__':
    a = delete_nth([20,37,20,21],1)
    print(a)
