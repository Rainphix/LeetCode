# class Solution:
#     def subsets(self, nums):
#         res = [[]]
#         for i in nums:
#             r_res = res.copy()
#             for j in r_res:
#                 res.append([i] + j)
#         return res


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(0, nums, res, [])
        return res

    def dfs(self, idx, nums, res, path):
        res.append(path)
        for i in range(idx, len(nums)):
            self.dfs(i + 1, nums, res, path + [nums[i]])
        return

if __name__ == '__main__':

    s = Solution()
    nums = [1,2,3]
    # nums = []
    ans = s.subsets(nums)
    print(ans)