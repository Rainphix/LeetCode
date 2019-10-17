class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        # import math
        #
        # dict = {}
        # list_ = []
        # list__ = []
        #
        # for i in range(len(points)):
        #     square = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        #     dict[square] = points[i]
        # list_= sorted(dict.keys())
        # for j in range(K):
        #     list__.append(dict[list_[j]])
        # return list__

        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]

if __name__ == '__main__':

    s = Solution()
    ans = s.kClosest([[1,1],[1,2],[1,3]],2)
    print(ans)