class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        str = ""
        self.generate(n,n,str,ans)
        return ans

    def generate(self,left,right,str,res):

        if left == 0 and right == 0:
            res.append(str)
            return
        if left > 0:
            self.generate(left-1,right,str+"(",res)
            print(res)
        if left < right:
            self.generate(left,right-1,str+")",res)
            print(res)

if __name__ == "__main__":

    s = Solution()
    ans = s.generateParenthesis(3)
    print(ans)
    exit()
