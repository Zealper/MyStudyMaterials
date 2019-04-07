from itertools import combinations_with_replacement

given_str, *none, number = input().split()
all_results = combinations_with_replacement(sorted(given_str), int(number))
for results in all_results:
    print(''.join(results))
