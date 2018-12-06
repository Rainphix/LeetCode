class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        spread = 0
        profit = 0

        for i in range(len(prices)-1):

            if prices[i+1] > prices[i]:
                spread = prices[i+1]-prices[i]
                profit += spread

        return  profit

if __name__ == '__main__':

    s = Solution()
    ans = s.maxProfit([7,1,5,3,6,4])
    print(ans)