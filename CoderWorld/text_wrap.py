def wrap(string, max_width):
    str_length = len(string)
    results = ''
    i = 0
    while True:
        if str_length > max_width:
            results += string[i:max_width+i] + '\n'
            i += max_width
            str_length -= max_width
        else:
            results += string[-str_length:] + '\n'
            break
    return results


if __name__ == '__main__':
    results_2 = wrap(string='ABCDEFGHIJKLIMNOQRSTUVWXYZ', max_width=4)
    print(results_2)

# def wrap(string, max_width):
#     return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
