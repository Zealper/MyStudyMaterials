# Complete the compareTriplets function below.


def compare_triplets(a, b):
    a_player = 0
    b_player = 0
    for index, number in enumerate(a):
        if number > b[index]:
            a_player += 1
        elif number < b[index]:
            b_player += 1
    return [a_player, b_player]


list()
