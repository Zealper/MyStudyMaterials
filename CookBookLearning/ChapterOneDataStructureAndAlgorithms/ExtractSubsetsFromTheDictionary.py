prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 10.75,
}

# Make a dictionary of all prices over 200
p1 = {key:value for key,  value in prices.items() if value > 200}
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}

print(p1)
print(p2)

p1 = dict((key, value) for key, value in prices.items() if value > 200)
p2 = dict((key, prices[key]) for key in prices.keys() & tech_names)
p3 = {key:prices[key] for key in prices.keys() & tech_names}
print(p1)
print(p2)
print(p3)
