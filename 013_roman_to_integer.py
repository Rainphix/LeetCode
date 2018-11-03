class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1、罗马数字转换成数字，利用字典将罗马数字的每个元素对应的值存储
        # 2、除了最后位外，从0位开始，判断是否小于后一位，小于则减，否则加
        # 3、最后直接加上最末位

        count = 0
        # I,V,X,L,C,D,M = 1,5,10,50,100,500,1000

        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s)):

            if i == len(s) - 1:
                count = count + dict[s[i]]
            else:
                if dict[s[i]] < dict[s[i + 1]]:
                    count = count - dict[s[i]]
                else:
                    count = count + dict[s[i]]
        return count

if __name__ == '__main__':

    print('True')

    s = Solution()
    anwser = s.romanToInt('LVIII')
    print(anwser)
