# from itertools import combinations
#
# given_str = input().split()
# given_str, *none, number = given_str
# i = 0
# while i < int(number):
#     i += 1
#     all_results = combinations(sorted(given_str), i)
#     for results in all_results:
#         result = ''.join(results)
#         print(result)

from itertools import combinations

s, n = input().split()

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print(''.join(j))