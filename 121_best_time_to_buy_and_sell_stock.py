class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #################################超时##################################
        #  length = len(prices)
        #
        # if length == 0 or length == 1:
        #     return 0
        # profit = []
        # out = 1
        # max = 0
        #
        # for i in range(length-1):
        #     out = 1
        #     max = 0
        #     if i == length:
        #         break
        #     else:
        #         while(i+out <= length-1):
        #             if max <= prices[i+out]-prices[i]:
        #                 max = prices[i+out]-prices[i]
        #                 out = out + 1
        #             else:
        #                 out = out + 1
        #     profit.append(max)
        #
        # return sorted(profit)[-1]
        #################################超时##################################

        if not prices:
            return 0

        max_profit,min_buyin = 0,2**31

        for i in range(len(prices)):

            min_buyin = min(min_buyin,prices[i])

            max_profit = max(max_profit, prices[i]-min_buyin)

        return max_profit




if __name__ == '__main__':

    profit = [7,1,5,3,6,4]
    # profit = [7,6,5,4,3,2,1]
    # profit = [1,2]
    s = Solution()
    ans = s.maxProfit(profit)
    print(ans)