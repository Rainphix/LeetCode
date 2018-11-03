class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        count = 0
        for i in range(len(digits)):

            count += digits[i] * pow(10,i)

        count = count + 1
        str_count = str(count)
        index = []
        for s in str_count:
            index.append(int(s))
        return index

if __name__ == '__main__':

    s = Solution()
    ans = s.plusOne([9,9,9])
    print(ans)
