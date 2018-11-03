class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= -pow(2,31) and x <= pow(2,31)-1:

            if x >= 0:

                remider = int(str(x)[::-1])
                return remider
            else:
                remider = int(str(abs(x))[::-1])
                return -remider
        else:
            return 0

        # x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
        # return x if x < 2147483648 and x >= -2147483648 else 0

if __name__ == '__main__':

    s = Solution()
    x = s.reverse(15342364690)
    print(x)
