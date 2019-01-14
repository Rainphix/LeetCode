class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        # import copy
        #
        # left = 0
        # right = len(heights) - 1
        #
        # cut_heights = copy.deepcopy(heights)
        #
        # rec_area = 0
        #
        # while (left <= right):
        #
        #     sort_heights = sorted(cut_heights)
        #
        #     min_plank = sort_heights[0]
        #
        #     temp_area = (right - left + 1) * min_plank
        #
        #     if rec_area < temp_area:
        #         rec_area = temp_area
        #
        #         # print(right)
        #     if heights[left] <= heights[right]:
        #
        #         left += 1
        #         del cut_heights[0]
        #     else:
        #         right -= 1
        #         cut_heights.pop()
        # return rec_area

        # i = 0
        # max_value = 0
        # stack = []
        # heights.append(0)
        #
        # while i < len(heights):
        #
        #     if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
        #         stack.append(i)
        #         i += 1
        #     else:
        #         now_idx = stack.pop()
        #
        #         if len(stack) == 0:
        #             max_value = max(max_value, i * heights[now_idx])
        #         else:
        #             max_value = max(max_value, (i - stack[-1] - 1) * heights[now_idx])
        #
        # return max_value

        # 核心思路：构造一个递增栈，来存储连续增加的木板长度
        # 当遇到比栈顶小的元素时，认定达到当前的最大值，清空栈，开始下一轮


        i = 0
        max_value = 0
        stack = []
        heights.append(0)

        while i < len(heights):

            print(i)
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:

                stack.append(i)
                i += 1

            else:

                value = stack.pop()

                if len(stack) == 0:
                    max_value = max(max_value, heights[value] * i)
                else:
                    max_value = max(max_value, heights[value] * (i - stack[-1] - 1))
                    print(i,stack[-1],max_value)
        return max_value



if __name__ == '__main__':

    s = Solution()
    ans = s.largestRectangleArea([5,5,5,7,1,1,5,2,7,6])
    # print(ans）
