
# 从序列中移除重复项且保持元素间顺序不变

# 序列中的值是可哈希（hashable）


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# 不可哈希的对象


def dedupe_2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    example = list(dedupe(a))
    print(example)
    print(dedupe(a))
    for i in dedupe(a):
        print(i)
