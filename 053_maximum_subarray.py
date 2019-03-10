# class Solution:
#     def maxSubArray(self, nums):
#
#         if len(nums) <= 1:
#             return sum(nums)
#
#         nums_count = []
#
#         for i in range(len(nums)):
#             nums_count.append((sum(nums[:i+1])))
#
#         max_num = nums_count.index(max(nums_count))
#         min_num = nums_count.index(min(nums_count))
#
#         if max_num < min_num:
#             return sum(nums[:max_num+1])
#         else:
#             return sum(nums[min_num+1 : max_num+1])
class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)

if __name__ == '__main__':

    s = Solution()
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [0,1,-1,4,-3,2,-1]
    nums = [1,2,-1]
    ans = s.maxSubArray(nums)
    print(ans)