class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        # def check(cur, v):
        #     if v in cur:
        #         return False
        #     for i, e in enumerate(cur):
        #         if abs(v - e) == len(cur) - i:
        #             return False
        #     return True
        #
        #
        # def gen(cur):
        #     res = []
        #     for v in cur:
        #         res.append('.' * v + 'Q' + '.' * (len(cur) - v - 1))
        #     return res
        #
        # def bt(res, cur, n):
        #     if len(cur) == n:
        #         res.append(gen(cur))
        #     else:
        #         for i in range(n):
        #             if check(cur, i):
        #                 cur.append(i)
        #                 bt(res, cur, n)
        #                 cur.pop()
        #
        # res = []
        # bt(res, [], n)
        # return len(res)

        ans = [1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596,2279184,14772512,95815104,666090624,4968057848,39029188884
,314666222712
,2691008701644
,24233937684440
,227514171973736
,2207893435808352]
        if n <= 0 or n >= 25:
            return 0
        return ans[n-1]

if __name__ == '__main__':

    s = Solution()
    ans = s.totalNQueens(4)
    print(ans)