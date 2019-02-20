
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

print(min(zip(prices.values(), prices.keys())))

print(max(zip(prices.values(), prices.keys())))
# zip函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
print(max(zip(prices.keys(), prices.values())))

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]

# 对数据排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print('prices sorted is {}'.format(prices_sorted))

# zip()创建一个迭代器，他的内容只能被消费一次，下面是错误代码
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
print(max(prices_and_names))

# 当value值相同时，将对比key
