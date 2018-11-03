class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 对数组进行排序
        # 设置三个指针，分别指向头，头+1，尾
        # 三数相加，如果为0，则添加进数组
        # 小于0，left+1，大于0，right+1

        size = len(nums)
        ans = []
        if size <= 2:
            return ans
        nums.sort()
        i = 0
        while i < size - 2:
            tmp = 0 - nums[i]
            j = i + 1
            k = size - 1
            while j < k:
                if nums[j] + nums[k] < tmp:
                    j += 1
                elif nums[j] + nums[k] > tmp:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k:
                        if nums[j] != nums[j - 1]:      # 进过上一次判断，去掉相同的
                            break
                        if nums[k] != nums[k + 1]:
                            break
                        j += 1
                        k -= 1
            i += 1
            while i < size - 2:
                if nums[i] != nums[i - 1]:
                    break
                i += 1
        return ans

if __name__ == '__main__':

    nums = sorted([-1, 0, 1, 2, -1, -4])
    # renums =[]
    # temp_append = []
    # temp_rest = []
    # temp = []
    #
    # for i in nums:
    #     temp_rest = nums
    #     temp_rest.remove(i)
    #     for j in temp_rest:
    #         temp_append.clear()
    #         rest = 0 - i - j
    #         temp_rest.remove(j)
    #         temp_append.append(i)
    #         temp_append.append(j)
    #         if rest in temp_rest:
    #             temp_append.append(rest)
    #             print(rest)
    #             renums.append(temp_append)
    #         temp_rest.append(j)
    #         temp_rest.sort()
    #
    # print(renums)

    print(True)
