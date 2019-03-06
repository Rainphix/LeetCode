class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            r_res = res.copy()
            for j in r_res:
                res.append([i] + j)
        return res

if __name__ == '__main__':

    s = Solution()
    nums = [1,2,3]
    # nums = []
    ans = s.subsets(nums)
    print(ans)