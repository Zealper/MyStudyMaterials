import heapq
import logging


class Solution(object):

    @classmethod
    def longest_palindrome(cls, s):
        """
        :type s: str
        :rtype: str
        """
        s_str = []
        for index, info in enumerate(s):
            s_list = []
            s_full = []
            index_before = index-1
            index_after = index+1
            try:
                while s[index_before] == s[index_after] and index != 0 and index != -1:
                    s_list.append(index)
                    if s[index_before] == s[index_after]:
                        s_list.append(index_after)
                        s_list.append(index_before)
                    index_after += 1
                    index_before -= 1
                if s[index] == s[index+1]:
                    s_list.append(index)
                    s_list.append(index+1)
                if s_list:
                    s_list.sort()
                    for num in s_list:
                        s_full.append(s[num])
                    s_full = ''.join(s_full)
                    if s_full:
                        s_str.append(s_full)
            except Exception as err:
                logging.error(err)
                pass
        if not s_str:
            return ""
        return heapq.nlargest(1, s_str)[0]


if __name__ == '__main__':
    yes = Solution()
    a = yes.longest_palindrome("babad")
    print(a)
