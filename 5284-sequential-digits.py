class Solution:
    def sequentialDigits(self, low: int, high: int):

        digit = [12,
                 23,
                 34,
                 45,
                 56,
                 67,
                 78,
                 89,
                 123,
                 234,
                 345,
                 456,
                 567,
                 678,
                 789,
                 1234,
                 2345,
                 3456,
                 4567,
                 5678,
                 6789,
                 12345,
                 23456,
                 34567,
                 45678,
                 56789,
                 123456,
                 234567,
                 345678,
                 456789,
                 1234567,
                 2345678,
                 3456789,
                 12345678,
                 23456789,
                 123456789]
        ans = []
        for i in digit:
            if i >= low and i<= high:
                ans.append(i)
        return ans

    def judgement(self, num):
        num_l = []
        for i in str(num):
            num_l.append(int(i))

        for i in range(1, len(num_l)):
            if num_l[i] != num_l[i - 1] + 1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    low, high = 1000, 13000
    print(s.sequentialDigits(low, high))
