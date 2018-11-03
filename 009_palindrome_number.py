class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x<0:
            return False

        x = str(x)
        l = len(x)

        for i in range(l):
            if x[i] != x[l - i - 1]:
                return False
                break
        return True

if __name__ == "__main__":

    s = Solution()
    k = s.isPalindrome(121212121212121212121212121212121212121212121)
    print(k)
