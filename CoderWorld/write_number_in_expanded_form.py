# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.
#
# If you liked this kata, check out part 2!!
#
def expanded_form(num):
    num_str = str(num)
    num_len = len(num)
    final_form = []
    for order, num in enumerate(num_str):
        if num != '0':
            num += '0'*(num_len-order-1)
            final_form.append(num)
    return ' + '.join(final_form)




if __name__ == '__main__':
    a = expanded_form('70304')
    print(a)
