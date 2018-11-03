<<<<<<< HEAD
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows <= 1 or numRows >= len(s):
            return s
        arr = [''] * numRows
        line, step = 0, -1
        for c in s:
            arr[line] += c
            print(arr)
            if line % (numRows - 1) == 0:
                step = - step
            line += step
        return ''.join(arr)


if __name__ == "__main__":

    s = Solution()
    ans = s.convert("PAYPALISHIRING",3)
    print(ans)
    exit()
=======
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
>>>>>>> eb70bef8345fcb2ba0b0e5c25a81918c6c191466
