# coding=utf-8
# 将序列分解为单独的变量

p = (4, 5)
x, y = p
print(x, y)

data = ['', 50, 91.1, (2012, 12, 21)]
name, share, price, date = data
print(name)
print(share)
print(price)
print(date)
name, share, price, (year, month, day) = date
print(year)
print(month)
print(day)
# 元素数量不匹配时，错误提示
_, shares, prince, _ = date
