# class Solution(object):
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         ans = ""
#         nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#         Roman = ["M", "D", "C", "L", "X", "V", "I"]
#         for idx in [0, 2, 4]:
#             k = int(num / nums[Roman[idx]])
#             re = int((num % nums[Roman[idx]]) / nums[Roman[idx + 2]])
#             ans += k * Roman[idx]
#             #for j in range(k):
#              #   ans += Roman[idx]
#             if re >= 9:
#                 ans += Roman[idx + 2] + Roman[idx]
#             elif re >= 5:
#                 ans += Roman[idx + 1] + (re - 5) * Roman[idx + 2]
#             elif re == 4:
#                 ans += Roman[idx + 2] + Roman[idx + 1]
#             else:
#                 ans += re * Roman[idx + 2]
#             num %= nums[Roman[idx + 2]]
#         return ans

class Solution(object): #大佬做法
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        token = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                 (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for n, t in token:
            while num >= n:
                res += t;
                num -= n
        return res



if __name__ == '__main__':

    s = Solution()
    ans = s.intToRoman(58)
    print(ans)