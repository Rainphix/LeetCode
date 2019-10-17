class Solution:
    def minCostToMoveChips(self, chips) -> int:
        if chips.count(chips[0]) == len(chips):
            return 0
        single = 0
        double = 0
        for i in chips:
            if i % 2 == 0:
                double = double + 1
            else:
                single = single + 1

        value = single if single <= double else double
        return value

if __name__ == '__main__':
    chips = [1, 2, 2, 4, 6, 8, 9, 10]
    s = Solution()
    print(s.minCostToMoveChips(chips))