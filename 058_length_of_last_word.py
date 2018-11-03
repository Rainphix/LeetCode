class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = s.split()
        if not string:
            print(len(string))
            return 0
        else:
            print(string)
            index = len(string[-1])
            print(len(' '))
            return index

if __name__ == '__main__':

    s = Solution()
    k = s.lengthOfLastWord('a ')
    print(k)

    # h = ' '
    # if not (h.split(' ')):
    #     print('not black')
