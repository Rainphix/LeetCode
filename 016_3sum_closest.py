class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #与015相似的思路 打败19.27%的提交记录
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(ans - target) > abs(temp - target):
                    ans = temp
                elif target < temp:
                    k -= 1
                else:
                    j += 1
        return ans

if __name__ == '__main__':


    nums = [0,1,0,1,0,2,5,52]
    target = 10
    s = Solution()
    ans = s.threeSumClosest(nums,target)
    print(ans)