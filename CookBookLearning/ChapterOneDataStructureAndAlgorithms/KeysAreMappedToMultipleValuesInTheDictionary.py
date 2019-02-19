# d = [{'a':[1, 2, 3], 'b':[4, 5]}]
# e = {'a':{1, 2, 3},
#      'b':{4, 5}}

# collections 学习

from collections import defaultdict


# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['a'].append(3)
# print(d)
#
# d = defaultdict(set)
# d['b'].add(4)
# d['b'].add(5)
# print(d)

# 另一种不常用的方法
# d = {}
# d.setdefault('a', []).append(1)
# d.setdefault('a', []).append(2)
# d.setdefault('a', []).append(3)

# 当自己做初始化时，一键多值字典很容易，但是比较乱, defaultdict可以让代码清晰

# pairs = {'a': 1, 'b': 2}
# d = {}
# for key, value in pairs.items():
#     if key not in d:
#         d[key] = [value]
# print(d)

# d = defaultdict(list)
# for key, value in pairs.items():
#     d[key].append(value)
# print(d)
