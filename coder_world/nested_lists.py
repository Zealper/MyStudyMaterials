marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])
    second_scores = sorted(list(set([m for n, m in students])))[1]
    print('\n'.join([n[1] for n in sorted(students) if n[0] == second_scores]))