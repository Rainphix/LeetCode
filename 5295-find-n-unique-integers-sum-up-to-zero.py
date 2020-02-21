from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        ans = []
        temp = 1
        if n%2 == 1:
            ans.append(0)
            for i in range((n-1)//2):
                ans.append(temp)
                ans.append(temp * (-1))
                temp += 1
        else:
            for i in range(n // 2):
                ans.append(temp)
                ans.append(temp * (-1))
                temp += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.sumZero(n))