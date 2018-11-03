class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        step = []
        step.append(1)
        step.append(1)
        for i in range(2,n+1):
            step.append(step[-1] + step[-2])
        return step[-1]



if __name__ == '__main__':

    s = Solution()
    ans = s.climbStairs(2)
    print(ans)
