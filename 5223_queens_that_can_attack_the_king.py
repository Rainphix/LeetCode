class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []

        def dfs(queens: List[List[int]], king: List[int], x: int, y: int, res: List):

            tmp_x, tmp_y = 0, 0
            while True:
                if king[0] + tmp_x >= 8 or king[0] + tmp_x < 0 or king[1] + tmp_y >= 8 or king[1] + tmp_y < 0:
                    return
                if [king[0] + tmp_x, king[1] + tmp_y] in queens:
                    res.append([king[0] + tmp_x, king[1] + tmp_y])
                    return
                else:
                    tmp_x += x
                    tmp_y += y

        dfs(queens, king, 1, 0, res)
        dfs(queens, king, 0, 1, res)
        dfs(queens, king, -1, 0, res)
        dfs(queens, king, 0, -1, res)
        dfs(queens, king, 1, -1, res)
        dfs(queens, king, -1, 1, res)
        dfs(queens, king, -1, -1, res)
        dfs(queens, king, 1, 1, res)
        return res

if __name__ == '__main__':
    solve = Solution()
    queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
    king = [0, 0]
    print(solve.queensAttacktheKing(queens, king))