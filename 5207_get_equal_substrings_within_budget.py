class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        n = len(s)
        record = []
        for i in range(n):
            record.append(abs(ord(t[i]) - ord(s[i])))

        start, end = 0, 0
        windowsum = 0
        res = 0
        for end in range(n):
            # print windowsum, start, end, res
            windowsum += record[end]

            while windowsum > maxCost:
                res = max(res, end - start)
                windowsum -= record[start]
                start += 1
        res = max(res, end - start + 1)
        return res

if __name__ == '__main__':
    s = "nfyvfrvrbinpwkepscnnzfyiuznrp"
    t = "eclliczkrezvhyvoyhbuurhkhtvto"
    so = Solution()
    print(so.equalSubstring(s,t,194))