class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #################################超时##################################
        # if not prices:
        #     return 0
        #
        # left_profit, right_profit = 0,0
        #
        # profit = 0
        #
        # def max_position(left,right):
        #
        #     max_profit, min_buyin = 0, 2 ** 31
        #
        #     for i in range(left,right):
        #
        #         min_buyin = min(min_buyin,prices[i])
        #         max_profit = max(max_profit, prices[i]-min_buyin)
        #
        #     return max_profit
        #
        # for i in range(len(prices)):
        #
        #     left_profit = max_position(0,i)
        #     right_profit = max_position(i,len(prices))
        #
        #     profit = max(profit,left_profit+right_profit)
        #
        # return profit
        # 不断遍历寻找能将区间划分为最大两个利润块的节点//超时了—_—||
        #################################超时##################################


        # 四个变量，分别表示第一次买完，第一次卖完，第二次买完，第二次卖完后手上的钱。
        #
        # 每次操作完都要保证手上的钱最多
        #
        # 第二买入的钱为前一次卖出所获的钱
        
        if not prices:
            return 0

        buy_1, buy_2 = -65516,-65516
        sell_1, sell_2 = 0,0

        for i in range(len(prices)):

            buy_1 = max(buy_1,-prices[i])
            sell_1 = max(sell_1,buy_1+prices[i])
            buy_2 = max(buy_2,sell_1-prices[i])
            sell_2 = max(sell_2,buy_2+prices[i])

        return sell_2



if __name__ == '__main__':

    s = Solution()
    ans = s.maxProfit([3,3,5,0,0,3,1,4])
    # ans = s.maxProfit([7,6,4,3,1] )
    print(ans)