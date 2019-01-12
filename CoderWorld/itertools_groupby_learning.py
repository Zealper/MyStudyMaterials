# from itertools import groupby
# number = input()
# specified_str= groupby(str(number))
# result_list = []
# for specified in specified_str:
#     result = (len(list(specified[1]))), int(specified[0])
#     result_list.append(str(result))
# print(' '.join(result_list))

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

