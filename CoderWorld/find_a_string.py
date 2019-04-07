
# 有问题来不起了
# In
# this
# challenge, the
# user
# enters
# a
# string and a
# substring.You
# have
# to
# print
# the
# number
# of
# times
# that
# the
# substring
# occurs in the
# given
# string.String
# traversal
# will
# take
# place
# from left to
#
# right, not
# from right to
#
# left.
#
# NOTE: String
# letters
# are
# case - sensitive.
#
# Input
# Format
#
# The
# first
# line
# of
# input
# contains
# the
# original
# string.The
# next
# line
# contains
# the
# substring.
#
# Constraints
#
# Each
# character in the
# string is an
# ascii
# character.
#
# Output
# Format
#
# Output
# the
# integer
# number
# indicating
# the
# total
# number
# of
# occurrences
# of
# the
# substring in the
# original
# string.
#
# Sample
# Input
#
# ABCDCDC
# CDC
# Sample
# Output
#
# 2
# Concept
#
# Some
# string
# processing
# examples, such as these, might
# be
# useful.
# There
# are
# a
# couple
# of
# new
# concepts:
# In
# Python, the
# length
# of
# a
# string is found
# by
# the
# function
# len(s), where is the
# string.
# To
# traverse
# through
# the
# length
# of
# a
# string, use
# a
# for loop:
#
# for i in range(0, len(s)):
#     print(s[i])
# A
# range
# function is used
# to
# loop
# over
# some
# length:
#
# range(0, 5)
# Here, the
# range
# loops
# over
# to. is excluded.


def count_substring(string, sub_string):
    number = 0
    string_list = list(string)
    string_list_sub = string_list[:-2]
    for i, j in enumerate(string_list_sub):
        for n in range(1, len(sub_string)):
            j += string_list[i+n]
        if j == sub_string:
            number += 1
    return print(number)


if __name__ == '__main__':
    count_substring('ACDC', 'CDC')


def count_substring(string, sub_string):
    return (sum([1 for i in range(0, len(string) - len(sub_string) + 1) if
                 (string[i:(len(sub_string) + i)] == sub_string)]))
