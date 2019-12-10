class Solution:
    def largestRectangleArea(self, heights):

        i = 0
        max_value = 0
        stack = []
        heights.append(0)

        while i < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                value = stack.pop()
                if len(stack) == 0:
                    max_value = max(max_value, heights[value] * i)
                else:
                    max_value = max(max_value, heights[value] * (i - stack[-1] - 1))
                    # print(i,stack[-1],max_value)
        return max_value

    def maximalRectangle(self, matrix) -> int:
        if len(matrix) == 0:
            return 0
        maxArea = 0
        histogram = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                histogram[j] = histogram[j]+1 if matrix[i][j] == '1' else 0
            maxArea = max(maxArea, self.largestRectangleArea(histogram))
        return maxArea

    # def maximalRectangle(self, matrix) -> int:
    #     # Except for the last test sample, the answers are all right
    #     # Time Limited
    #     if len(matrix) == 0:
    #         return 0
    #     for i in range(0, len(matrix)):
    #         for j in range(0, len(matrix[i])):
    #             matrix[i][j] = int(matrix[i][j])
    #
    #     for i in range(0, len(matrix)):
    #         for j in range(1, len(matrix[i])):
    #             matrix[i][j] = int(matrix[i][j-1]) + 1 if matrix[i][j] == 1 else 0
    #     print(matrix)
    #     maxArea = 0
    #
    #     for i in range(0, len(matrix)):
    #         for j in range(0, len(matrix[i])):
    #             maxWidth = matrix[i][j]
    #             for k in range(i, -1, -1):
    #                 maxWidth = min(maxWidth, matrix[k][j])
    #                 curArea = maxWidth * (i-k+1)
    #                 maxArea = max(maxArea, curArea)
    #
    #     return maxArea

    def dp(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0] * n
        right = [0] * n
        height = [0] * n

        maxarea = 0

        for i in range(m):
            cur_left = 0
            cur_right = n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j+1
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea



if __name__ == '__main__':
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    s = Solution()
    print(s.maximalRectangle(matrix))