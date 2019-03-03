# class Solution: # 作弊解法
#     def permute(self, nums):
#         import itertools
#         return list(itertools.permutations(nums))

class Solution:
    def permute(self, nums):

        res = []
        if len(nums) == 1:  # 结束条件
            return [nums]
        if len(nums) == 2:  # 结束条件
            return [nums, nums[::-1]]
        for i in range(len(nums)):
            num = nums[i]
            newnums = nums[:i] + nums[i+1:]
            for item in self.permute(newnums):  # 递归调用
                res.append([num] + item)
        return res

if __name__ == '__main__':

    s = Solution()
    ans = s.permute([1,2,3,5,6,8])
    print(ans)