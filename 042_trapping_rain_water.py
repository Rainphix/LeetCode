class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)

        if length < 2:
            return 0
        leftMax = 0
        rightMax = 0
        water = 0
        for i in range(1,length-1):

            for j in range(0,i):
                leftMax = max(leftMax,height[j])
            for j in range(i+1,length):
                rightMax = max(rightMax,height[j])

            min_level = min(leftMax,rightMax)
            if min_level > height[i]:
                water += min_level - height[i]

        return water

if __name__ == "__main__":

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    #height = [2,1,2]
    sol = Solution()
    ans = sol.trap(height)
    print(ans)
    exit()