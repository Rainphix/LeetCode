class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums[:] = sorted(list(set(nums)))
        return len(nums)

if __name__ == '__main__':

    s = Solution()
    ans = s.removeDuplicates([1,1,2])
    print(ans)