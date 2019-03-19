# 对切片命名

record = '.........100........513.25'
cost = record[20: 23] * int(record[-1: -5])

# 对切片进行变量命名
SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost_2 = int(record[SHARES]) * int(record[PRICE])
