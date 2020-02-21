from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        res = 0
        closed_box = [0] * 1010
        q = []

        for i in initialBoxes:
            if status[i]:
                q.append(i)
            else:
                closed_box[i] = 1

        while q:
            cur = q.pop(0)
            for i in keys[cur]:
                status[i] = 1

                if closed_box[i]:
                    q.append(i)
                    closed_box[i] = 0
            res += candies[cur]

            for i in containedBoxes[cur]:
                if status[i]:
                    q.append(i)
                else:
                    closed_box[i] = 1
        return res


if __name__ == "__main__":

    s = Solution()
    status = [1, 0, 1, 0]
    candies = [7, 5, 4, 100]
    keys = [[], [], [1], []]
    containedBoxes = [[1, 2], [3], [],[]]
    initialBoxes = [0]
    print(s.maxCandies(status,candies,keys,containedBoxes,initialBoxes))