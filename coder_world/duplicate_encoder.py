#The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples:
# #
# # "din" => "((("
# #
# # "recede" => "()()()"
# #
# # "Success" => ")())())"
# #
# # "(( @" => "))(("

# def duplicate_encode(word):
#     word_new = []
#     for w in word:
#         word_number = word.lower().count(w.lower())
#         print(w, word_number)
#         if word_number != 1:
#             w = ')'
#             word_new.append(w)
#         else:
#             w = '('
#             word_new.append(w)
#     return ''.join(word_new)
#
# if __name__ == '__main__':
#     a = duplicate_encode("w@QRlR(cQbPbRk))FTTT")
#     print(a)


