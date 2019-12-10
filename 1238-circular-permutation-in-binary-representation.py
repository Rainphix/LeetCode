class Solution:
    # def circularPermutation(self, n, start):
    #     return [start^i^(i >> 1) for i in range(1 << n)]

    def circularPermutation(self, n: int, start: int):
        res = list()
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        while res[0] != start:
            res.append(res.pop(0))
        return res



if __name__ == '__main__':
    s = Solution()
    n = 2
    start = 3
    print(s.circularPermutation(n, start))