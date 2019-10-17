class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 198是 打家劫舍i

        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)

        total = [0] * len(nums)
        total[0] = nums[0]
        total[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            total[i] = max(total[i - 2] + nums[i], total[i - 1])

        return total[len(nums) - 1]


if __name__ == '__main__':
    print(True)