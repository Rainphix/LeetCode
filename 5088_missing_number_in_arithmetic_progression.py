class Solution:
    def missingNumber(self, arr) -> int:
        sub_cost = (arr[-1] - arr[0]) / (len(arr))
        if sub_cost == 0:
            return 0
        for i in range(len(arr)):
            if arr[i] + sub_cost != arr[i+1]:
                return int(arr[i] + sub_cost)


if __name__ == '__main__':

    s = Solution()
    arr = [15,13,12]
    print(s.missingNumber(arr))