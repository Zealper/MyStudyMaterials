import os

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# Determine if any .py files exist in a directory
files = os.listdir('# dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [{'name': 'GOOG', 'shares': 50},
             {'name': 'YHOO', 'shares': 75},
             {'name': 'AOl', 'shares': 20},
             {'name': 'SCOX', 'shares': 65}]
s = sum((x * x for x in nums))  # Pass generator-expr as argument
s2 = sum(x * x for x in nums)  # More element syntax
nums = [1, 2, 3, 4, 5]
s3 = sum([x * x for x in nums])
# Original: Return 20
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
