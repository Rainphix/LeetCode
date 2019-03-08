class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def check(cur, v):
            if v in cur:
                return False
            for i, e in enumerate(cur):
                if abs(v - e) == len(cur) - i:
                    return False
            return True


        def gen(cur):
            res = []
            for v in cur:
                res.append('.' * v + 'Q' + '.' * (len(cur) - v - 1))
            return res

        def bt(res, cur, n):
            if len(cur) == n:
                res.append(gen(cur))
            else:
                for i in range(n):
                    if check(cur, i):
                        cur.append(i)
                        bt(res, cur, n)
                        cur.pop()

        res = []
        bt(res, [], n)
        return res

if __name__ == '__main__':

    s = Solution()
    ans = s.solveNQueens(7)
    print(ans)