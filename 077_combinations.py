class Solution:
    def combine(self, n, k):
        res = []
        if n <= 0 or k <= 0 or n < k:
            return res

        nums = []
        self.com(n, k, 1, nums, res)
        return res

    def com(self, n, k, start, nums, res):

        if len(nums) == k:
            res.append(nums.copy())
            return

        for i in range(start, n-(k - len(nums)) + 2): # 不需要遍历到最后

            nums.append(i)
            self.com(n, k, i+1, nums, res)
            nums.pop()  # 每次删除末尾元素重新添加

if __name__ == '__main__':

    s = Solution()
    # res = [
    #       [1,2],
    #       [1,3],
    #       [1,4],
    #       [2,3],
    #       [2,4],
    #       [3,4],
    #     ]
    ans = s.combine(7,6)
    print(ans)
