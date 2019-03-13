class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = []
        for row_list in range(rowIndex+1):
            row = [None for i in range(row_list + 1)]
            row[0] = 1
            row[-1] = 1
            # print(row)
            for num in range(1, len(row) - 1):
                row[num] = triangle[row_list - 1][num - 1] + triangle[row_list - 1][num]

            triangle.append(row)
        return triangle[-1]

if __name__ == '__main__':
    s = Solution()
    ans = s.getRow(3)
    print(ans)
