# coding = utf-8

from operator import itemgetter

rows = [{'fname': 'Brian', "lname": "Jones", "uid": 1003},
        {'fname': 'David', "lname": "Beazley", "uid": 1002},
        {'fname': 'John', "lname": "Cleese", "uid": 1001},
        {"fname": "Big", "lname": "Jones", "uid": 1004}]
rows_by_name = sorted(rows, key=itemgetter("fname"))
rows_by_uid = sorted(rows, key=itemgetter("uid"))
rows_by_lname = sorted(rows, key=itemgetter("lname"))

print(rows_by_lname)
print(rows_by_name)
print(rows_by_uid)
