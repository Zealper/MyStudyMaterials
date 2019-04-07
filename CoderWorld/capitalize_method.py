def solve(s):
    return ' '.join(i.capitalize() for i in s.split(' '))


if __name__ == '__main__':
    print(solve('alan ken'))
