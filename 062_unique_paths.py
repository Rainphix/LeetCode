class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 排列组合的方式
        x = 1
        y = 1
        min_num = min(m,n)
        max_num = max(m,n)

        i = max_num
        while(i<=m+n-2):

            y*=i
            i+=1

        for j in range(1,min_num):
            # print(j)
            x*=j
        # print(y,x)
        return int(y/x)


if __name__ == '__main__':

    # m = 3, n = 2 3
    # m = 7, n = 3 28

    print("がんばって")

    s = Solution()
    ans = s.uniquePaths(5,4)
    print(ans)
