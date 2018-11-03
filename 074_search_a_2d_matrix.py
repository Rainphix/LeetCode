class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        exist = False
        for i in matrix:

            if target in i:
                exist = True

                break
        return exist


if __name__ == '__main__':
    matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    exist = False
    target = 13
    for i in matrix:

        if target in i:

            exist = True

            break
    print(exist)
