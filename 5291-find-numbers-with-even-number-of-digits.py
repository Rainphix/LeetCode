from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        if not nums:
            return ans
        for i in nums:
            temp = str(i)
            if (len(temp))%2 == 0:
                ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [555,901,482,1771]
    print(s.findNumbers(nums))