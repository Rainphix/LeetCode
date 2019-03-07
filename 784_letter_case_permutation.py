class Solution:
    def letterCasePermutation(self, S):

        res = []
        self.recursion(S, res, 0)
        return res

    def recursion(self, S, start, res):

        for i in range(len(S)):
            if S[i].isalpha():
                change = S[i].upper()
                S.replace()

            self.recursion(S, i, res)

        if start == len(S):
            res.append(S)
            return

if __name__ == '__main__':

    s = Solution()
    ans = s.letterCasePermutation('aaabbb')
    print(ans)