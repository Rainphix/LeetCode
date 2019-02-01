class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_level = 0
        move_peak = 0
        water = 0

        for i in range(1,len(height)):
           if height[max_level] < height[i]:
               max_level = i

        for i in range(0,max_level):

            if move_peak < height[i]:
                move_peak = height[i]
            else:
                water += move_peak - height[i]

        move_peak = 0

        for i in range(len(height)-1, max_level, -1):

            if move_peak < height[i]:
                move_peak = height[i]
            else:
                water += move_peak - height[i]

        return water


if __name__ == "__main__":

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    #height = [2,1,2]
    sol = Solution()
    ans = sol.trap(height)
    print(ans)
    exit()