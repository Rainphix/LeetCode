class Solution:
    def canJump(self, nums):

        jump_index = 0
        for i in range(len(nums)):
            if i > jump_index or jump_index >= len(nums) - 1:
                break
            jump_index = max(jump_index, i+nums[i])
        return jump_index >= len(nums) - 1

if __name__ == '__main__':

    s = Solution()
    nums = [2,3,1,1,4]
    ans = s.canJump(nums)
    print(ans)