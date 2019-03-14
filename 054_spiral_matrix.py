class Solution:
    def spiralOrder(self, matrix):

        for i in range(len(matrix)):

            for j in i:
                print(j)

        return False

if __name__ == '__main__':

    s = Solution()
    matrix = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]]
    ans = s.spiralOrder(matrix)
    print(True)