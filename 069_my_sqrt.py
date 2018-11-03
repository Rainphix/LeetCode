class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math

        sq = math.sqrt(x)

        return int(sq)

if __name__ == '__main__':

    s = Solution()
    ans = s.mySqrt(100)
    print(ans)

    print(True)
