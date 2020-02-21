from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        pos, ans = 0, 0
        static = {}
        while pos + minSize <= len(s):
            string = s[pos: pos+minSize]
            d = Counter(string)
            if len(d) > maxLetters:
                pos += 1
            else:
                if static.get(string) != None:
                    static[string] += 1
                else:
                    static[string] = 1
                pos += 1
        for i in static.values():
            ans = max(ans, i)

        return ans

if __name__ == '__main__':
    s = Solution()
    string = "aababcaab"
    maxLetters, minSize, maxSize = 2, 3, 4
    print(s.maxFreq(string, maxLetters, minSize, maxSize))