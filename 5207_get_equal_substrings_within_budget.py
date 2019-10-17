class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        if maxCost == 0:
            return 1

        size = len(s)
        list_s = list(s)
        list_t = list(t)
        sub = []

        for i in range(0, size):
            sub.append(abs(ord(list_s[i]) - ord(list_t[i])))
        print(sub)
        if maxCost >= sum(sub):
            return size

        start = 0
        end = 0
        maxsize = 0
        current_cost = 0

        while(end < size):
            current_cost = current_cost + sub[end]
            if current_cost == maxCost:
                maxsize = end - start + 1 if maxsize < end - start + 1 else maxsize
                current_cost = current_cost - sub[start]
                start = start + 1
                end = end + 1
            elif current_cost > maxCost:
                maxsize = end - start if maxsize < end - start else maxsize
                current_cost = current_cost - sub[start]
                start = start + 1
                end = end + 1
            else:
                end = end + 1

        return maxsize

if __name__ == '__main__':
    s = "nfyvfrvrbinpwkepscnnzfyiuznrp"
    t = "eclliczkrezvhyvoyhbuurhkhtvto"
    so = Solution()
    print(so.equalSubstring(s,t,194))