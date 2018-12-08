class Solution:
    import copy
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #################################超时##################################
        # def MinSum(x,y):
        #
        #     if x == len(triangle):
        #         return 0
        #
        #     left = MinSum(x+1,y)
        #     right = MinSum(x+1,y+1)
        #     ans = min(left,right) + triangle[x][y]
        #     print(ans)
        #     return min(left,right) + triangle[x][y]
        #
        # ans_min = MinSum(0,0)
        # return ans_min
        #################################超时##################################

        # 使用 O(n) 的额外空间
        # 动态规划 规定一个MinNum数组，来记录每次的最短路径

        MinNum = triangle[-1].copy()

        for i in reversed(range(len(triangle))):
            for j in range(i):
                MinNum[j] = min(MinNum[j],MinNum[j+1]) + triangle[i-1][j]
        ans = MinNum[0]
        return ans

if __name__ == '__main__':

    s = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    #triangle = [[-1],[-2,-3]]
    #triangle = [[1],[1,2],[1,2,3]]
    ans = s.minimumTotal(triangle)
    print(ans)
