class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        position_dict = {}
        for n in range(8):
            position_dict[n] = False
        line_list = []
        i = king[0]
        j = king[1]

        for n in queens:
            if n[0] == i:
                pass
            if n[1] == j:
                pass
            if abs(n[0]-i) == abs(n[1]-j):
                pass

        return line_list

if __name__ == '__main__':
    solve = Solution()
    queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
    king = [0, 0]
    print(solve.queensAttacktheKing(queens, king))

    laboratory = [1,0,0,0,0,0,0,0,0]
    dormitory = [0,1,0,0,0,0,0,0,0]
    refectory = [0,0,0,0,0,0,0,0,1]