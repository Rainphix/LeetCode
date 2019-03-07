# class Solution:
#     def letterCasePermutation(self, S):
#
#         res = []
#         self.recursion(S, 0, res)
#         return res
#
#     def recursion(self, S, start, res):
#
#         for i in range(start, len(S)):
#
#             s_change = S
#             if not s_change[i].isdigit():
#                 s_change[:i+1].replace(s_change[i], s_change[i].upper())
#                 print(True)
#             self.recursion(s_change, i+1, res)
#
#         if start == len(S):
#             res.append(S)
#             return

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return [S]
        rest = self.letterCasePermutation(S[1:])
        if S[0].isalpha():
            return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]
        return [S[0] + s for s in rest]


if __name__ == '__main__':

    s = Solution()
    ans = s.letterCasePermutation('aaaaaa')
    print(ans)