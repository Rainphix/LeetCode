class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return None

        spring = nums
        self.count = [None] * len(spring)
        self.count[0] = spring[0]
        for k in range(1,len(spring)):
            self.count[k] = self.count[k-1] + spring[k]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.count[j]
        else:
            return self.count[j] - self.count[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':

    #nums = [1,1,5,8,2,5,2,58,6589,24]
    nums = [-2, 0, 3, -5, 2, -1]
    i,j = 0,5
    obj = NumArray(nums)
    param_1 = obj.sumRange(i,j)
    print(param_1)