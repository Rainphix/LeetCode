class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        begin = 0
        end = len(height) - 1
        process = True
        short_plate = 0
        water_vector = 0
        water_temple = 0

        while (process == True):

            if height[begin] <= height[end]:
                short_plate = height[begin]
                begin = begin + 1
            else:
                short_plate = height[end]
                end = end - 1

            water_temple = short_plate * (end - begin + 1)

            if water_vector < water_temple:
                water_vector = water_temple

            if begin == end:
                process = False

        return water_vector

if __name__ == '__main__':

    s = Solution()
    anwser = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(anwser)
