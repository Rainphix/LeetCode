class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:

        difference = abs(difference)
        rvalue = 0

        if difference == 0:
            for e in arr:
                if arr.count(e) > rvalue:
                    rvalue = arr.count(e)
            return rvalue

        # arr = sorted(arr)

        diff = {}
        maxSize = {}
        for i in range(0, difference):
            diff[i] = []
            maxSize[i] = 1

        for e in range(0, len(arr)):
            if diff[arr[e] % difference] == []:
                diff[arr[e] % difference].append(arr[e])
            else:
                if arr[e] not in diff[arr[e] % difference]:
                    if diff[arr[e] % difference][-1] + difference == arr[e]:
                        diff[arr[e] % difference].append(arr[e])
                    else:
                        diff[arr[e] % difference] = []
                        diff[arr[e] % difference].append(arr[e])
                        if len(diff[arr[e] % difference]) >= maxSize[arr[e] % difference]:
                            maxSize[arr[e] % difference] = len(diff[arr[e] % difference])

        for i in range(0, difference):
            maxSize[i] = maxSize[i] if maxSize[i] > len(diff[i]) else len(diff[i])
            if maxSize[i] > rvalue:
                rvalue = maxSize[i]
        return rvalue

if __name__ == '__main__':

    s = Solution()
    arr = [3,0,-3,4,-4,7,6]
    difference = 3
    print(s.longestSubsequence(arr, difference))