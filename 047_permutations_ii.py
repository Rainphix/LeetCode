# class Solution: # 作弊解法
#
#     def permuteUnique(self, nums):
#         import itertools
#         return self.delete_repeat(list(itertools.permutations(nums)))
#
#     def delete_repeat(self,list):
#         l = []
#         for i in list:
#             if i not in l:
#                 l.append(i)
#             else:
#                 pass
#         return l

class Solution: # 有误... [1,1]输出[[1,1],[1,1]]

    def permuteUnique(self, nums):

        res = []
        if len(nums) == 1:  # 结束条件
            return [nums]
        if len(nums) == 2:  # 结束条件
            return [nums, nums[::-1]]
        for i in range(len(nums)):
            num = nums[i]
            newnums = nums[:i] + nums[i+1:]
            for item in self.permuteUnique(newnums):  # 递归调用
                res.append([num] + item)

        return self.delete_repeat(res)

    def delete_repeat(self,list):
        l = []
        for i in list:
            if i not in l:
                l.append(i)
            else:
                pass
        return l


if __name__ == '__main__':

    s = Solution()
    nums = [1,1]
    ans = s.permuteUnique(nums)
    print(ans)