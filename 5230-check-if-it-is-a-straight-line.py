class Solution:
    def checkStraightLine(self, coordinates) -> bool:

        coordinates = sorted(coordinates)
        vertical = True
        for c in range(len(coordinates)-1):
            if coordinates[c][0] != coordinates[c+1][0]:
                vertical = False
        if vertical == True:
            return True


        gradient = []
        for i in range(len(coordinates)-1):
            if coordinates[i+1][0] - coordinates[i][0] != 0:
                gradient.append((coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0]))
            else:
                return False

        for g in range(len(gradient)-1):
            if gradient[g] != gradient[g+1]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    coordinates = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]]
    print(s.checkStraightLine(coordinates))