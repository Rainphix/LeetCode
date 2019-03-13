class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for row_list in range(numRows):
            row = [None for i in range(row_list+1)]
            row[0] = 1
            row[-1] = 1
            #print(row)
            for num in range(1, len(row)-1):
                row[num] = triangle[row_list-1][num-1] + triangle[row_list-1][num]

            triangle.append(row)
        return triangle


if __name__ == '__main__':

    s = Solution()
    ans = s.generate(5)
    print(ans)