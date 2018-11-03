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

    #     print(True)
    # # height = [1,8,6,2,5,4,8,3,7]
    # height = [1,1,1,11,1,1,1,1,1,1,1,1]
    # print(height[len(height)-1])
    # begin = 0
    # end = len(height)-1
    # process = True
    # short_plate = 0
    # water_vector = 0
    # water_temple = 0
    # while(process == True):
    #
    #     print('当前:', begin,end)
    #
    #
    #     if height[begin] <= height[end]:
    #         short_plate = height[begin]
    #         begin = begin + 1
    #     else:
    #         short_plate = height[end]
    #         end = end - 1
    #
    #     water_temple = short_plate*(end-begin+1)
    #
    #     if water_vector < water_temple:
    #         water_vector = water_temple
    #
    #     if begin == end:
    #         process = False
    #
    # print(water_vector)

    s = Solution()
    anwser = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(anwser)
