import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

if __name__ == '__main__':

    s = Solution()
    ans = s.isPalindrome("A man, a plan, a canal: Panama")
    print(ans)