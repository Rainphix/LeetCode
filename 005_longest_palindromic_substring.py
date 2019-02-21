class Solution(object):

    def huiwen(self,s):

        l = len(s)

        for i in range(l):
            if s[i] != s[l - i - 1]:
                return False
                break
        return True


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        string_origin = ''
        number = 0
        max_string = ''
        index = 0
        for i in s:

            string_origin = string_origin + i

            if i in string_origin:

                index = string_origin.find(i)

                l = self.huiwen(string_origin[index:])

                if l == True:

                    number = len(string_origin[index:])
                    if len(max_string) < number:
                        max_string = string_origin[index:]
            else:

                string_origin = string_origin + i

        return max_string

if __name__ == '__main__':

    s = Solution()
    max = s.longestPalindrome("babadada")
    print(max)
