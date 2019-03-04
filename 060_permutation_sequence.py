# class Solution: # 答案为['111', '112', '113', '121', '122', '123', '131', '132', '133', '211', '212', '213', '221', '222', '223', '231', '232', '233', '311', '312', '313', '321', '322', '323', '331', '332', '333']
#                 # 233 这写法也超时
#     def getPermutation(self, n, k): # n:元素个数 k:第k个排列
#
#         res = []
#         string = ''
#
#         self.recursion(n, 1, string, res)
#         print(res)
#
#         return str(res[k])
#
#     def recursion(self,n, start, string, res):
#
#         if n == len(string):
#             res.append(string)
#             return
#
#         for i in range(1, n+1):
#             string += str(i)
#             self.recursion(n, i + 1, string, res)
#             string = string[:-1]

# class Solution:     # Time Limited
#     def getPermutation(self, n, k): # n:元素个数 k:第k个排列
#
#         string = ''
#         nums = [i for i in range(1, n+1)]
#         res = self.permute(nums)
#         for j in res[k-1]:
#             string += str(j)
#         return string
#
#     def permute(self, nums):
#
#         res = []
#         if len(nums) == 1:  # 结束条件
#             return [nums]
#         if len(nums) == 2:  # 结束条件
#             return [nums, nums[::-1]]
#         for i in range(len(nums)):
#             num = nums[i]
#             newnums = nums[:i] + nums[i+1:]
#             for item in self.permute(newnums):  # 递归调用
#                 res.append([num] + item)
#         return res

class Solution:
    def getPermutation(self, n, k): # n:元素个数 k:第k个排列
        return True

if __name__ == '__main__':

    s = Solution()
    ans = s.getPermutation(3,3)
    print(ans)