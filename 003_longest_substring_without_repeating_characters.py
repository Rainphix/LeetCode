class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 原答案
        # l = len(s)
        # i = 0
        # longest_amount = 0
        # amount = 0
        # longest_str = {}
        #
        # while(i<l):
        #
        #     if s[i] not in longest_str:
        #
        #         longest_str[s[i]] = i
        #         amount = amount+1
        #         # print(amount)
        #         if longest_amount < amount:
        #             longest_amount = amount
        #
        #     else:
        #         i = i-amount+1
        #         amount = 1
        #         longest_str.clear()
        #         longest_str[s[i]] = i
        #
        #     i = i+1
        # return longest_amount

        maxlength = start = 0

        l = len(s)

        for i in range(0,l):

            if s[i] in s[start:i]:
                start = s.index(s[i],start) + 1
            else:
                maxlength = max(maxlength, i - start + 1)
        return maxlength


if __name__ == '__main__':

    S = Solution()
    inter = S.lengthOfLongestSubstring("dedf")
    s = "dedf"
    print(inter)
