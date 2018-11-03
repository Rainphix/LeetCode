class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # 创建字母对应的字符列表的字典
        dic = {2: ['a', 'b', 'c'],
               3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'],
               9: ['w', 'x', 'y', 'z'],
               }
        # 存储结果的数组
        # ret_str = []
        # if len(digits) == 0: return []
        # # 递归出口，当递归到最后一个数的时候result拿到结果进行for循环遍历
        # if len(digits) == 1:
        #     return dic[int(digits[0])]
        # # 递归调用
        # # print(ret_str)
        # result = self.letterCombinations(digits[1:])
        # print(result)
        #
        # # result是一个数组列表，遍历后字符串操作，加入列表
        # for r in result:
        #     for j in dic[int(digits[0])]:
        #         ret_str.append(j + r)
        # return ret_str


        ret_ans = []

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return dic[int(digits[0])]

        result = self.letterCombinations(digits[1:])

        for i in result:
            for j in dic[int(digits[0])]:
                ret_ans.append(j+i)
        return ret_ans


if __name__ == '__main__':

    dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    string = '234'

    combine = []

    s = Solution()
    ans = s.letterCombinations("2345")
    print(ans)
