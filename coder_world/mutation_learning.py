def mutate_string(string, position, character):
    str_list = [s for s in string]
    str_list[position] = character
    return ''.join(str_list)

if __name__ == '__main__':
    mutate_string('abcdefg', 1, '1')