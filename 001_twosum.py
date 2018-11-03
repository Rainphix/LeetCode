# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(0,len(nums)):
#
#             rest = target - nums[i]
#
#             if rest in nums:
#
#                 try:
#                     inter = nums.index(rest)
#
#                     if i == inter:
#
#                         inter = nums.index(rest,inter+1)
#
#                         if inter == None:
#
#                             pass
#
#                         else:
#
#                             return i,inter
#                             break
#
#                     else:
#
#                         return i,inter
#                         break
#
#                 except:
#
#                     pass

# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dic = {}
#         for i, num in enumerate(nums):
#             if (target - num) in dic:
#                 return i,dic[target - num]
#             dic[num] = i


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        l = len(nums)

        for i in range(l):

            if nums[i] in dict:

                return [dict[nums[i]],i]

            dict[target-nums[i]] = i


if __name__ == "__main__":

    # nums = []
    nums = [6,4,1,3,5,0]
    S = Solution()
    s = S.twoSum(nums,6)
    print(s)


