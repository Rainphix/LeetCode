class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        # solution: 贪心双指针
        # step1: 将人员按照重量从小到大进行排序
        # step2: 设置指针分别指向头和尾
        # step3: 若该人员无法与当前最轻的人同坐一条船，则只能单坐一船
        # step4: 若能同坐一船，各自移一位，否则，只移动尾部指针
        # step5: 返回计数

        i = 0
        j = len(people) - 1
        ans = 0

        people = sorted(people)

        while (i <= j):
            ans += 1
            if (people[i] + people[j] <= limit):
                i += 1
            j -= 1

        return ans

if __name__ == '__main__':

    # people = [1,2,4,3,5,6,7,8,4,3]
    # limit = 10
    #
    # i = 0
    # j = len(people) - 1
    # ans = 0
    #
    # people = sorted(people)
    #
    # while(i<=j):
    #     ans += 1
    #     if (people[i] + people[j] <= limit):
    #         i += 1
    #     j -= 1
    # print(ans)


    s = Solution()
    ans = s.numRescueBoats([3,5,3,4],5)
    print(ans)