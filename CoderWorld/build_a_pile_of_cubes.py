def find_nb(m):
    # your code
    n = (-1 + (1 + 8*(m**0.5))**0.5) / 2
    if n.is_integer():
        return int(n)
    else:
        return -1
#
# def find_nb(m):


if __name__ == "__main__":
    a = find_nb(5547014275991760785)
    print(a)
