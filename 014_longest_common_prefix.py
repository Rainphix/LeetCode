class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        for i in strs:
            print(i)



if __name__ == "__main__":

    s = Solution()
    string = ["flower","flow","flight"]
    ans = s.longestCommonPrefix(string)
    print("beautiful!")