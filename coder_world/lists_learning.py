# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Input Format
#
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(input())
    list_1 = []
    for _ in range(N):
        action = input().split()
        if action[0] == 'insert':
            list_1.insert(int(action[1]), int(action[2]))
        elif action[0] == 'print':
            print(list_1)
        elif action[0] == 'remove':
            list_1.remove(int(action[1]))
        elif action[0] == 'append':
            list_1.append(int(action[1]))
        elif action[0] == 'sort':
            list_1.sort()
        elif action[0] == 'pop':
            list_1.pop()
        elif action[0] == 'reverse':
            list_1.reverse()

# n = input()
# l = []
# for _ in range(n):
#     s = raw_input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print l


# eval('arr.{0}{1}'.format(cmd,tuple(map(int,arg))))
#
# #instead of 
#
# cmd += "("+ ",".join(args) +")"
#     eval("l."+cmd)
#             #and  It works
