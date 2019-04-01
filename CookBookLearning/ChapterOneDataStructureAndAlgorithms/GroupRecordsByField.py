from operator import itemgetter
from itertools import groupby
from collections import defaultdict


rows = [
    {"address": "5412 N CLARK", "date": "07/01/2012"},
    {"address": "5148 N CLARK", "date": "07/04/2012"},
    {"address": "5800 N CLARK", "date": "07/02/2012"},
    {"address": "2122 N CLARK", "date": "07/03/2012"},
    {"address": "5645 N CLARK", "date": "07/02/2012"},
    {"address": "1060 N CLARK", "date": "07/02/2012"},
    {"address": "4801 N CLARK", "date": "07/01/2012"},
    {"address": "1039 N CLARK", "date": "07/04/2012"},
]

# Sort by the desired field first

rows.sort(key=itemgetter('date'))

# iterate in range
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
    print(rows_by_date)
