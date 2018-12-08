class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        setor = set(nums)
        if len(setor) == len(nums):
            return False
        else:
            return True

if __name__ == '__main__':

    s = Solution()
    ans = s.containsDuplicate([1,2,3,1])
    print(ans)