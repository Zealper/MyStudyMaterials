from itertools import permutations


def all_result(given_str):

    given_str, *_,  number= given_str.split(' ')
    all_results = permutations(sorted(given_str), int(number))
    for result in all_results:
        result = ''.join(result)
        print(result)


if __name__ == '__main__':
    a = all_result('HACK 3')
    # for b in a:
    #     print(b)

# from itertools import permutations
# s,n = input().split()
# print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
