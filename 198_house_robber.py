class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return max(nums)

        total = [0] * len(nums)
        total[0] = nums[0]
        total[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            total[i] = max(total[i-2]+nums[i],total[i-1])

        return total[len(nums) - 1]


if __name__ == '__main__':

    s = Solution()
    # robber = [1,2,3,1]
    # robber = [2,7,9,3,1]
    robber = [2,1,1,2]
    ans = s.rob(robber)
    print(ans)