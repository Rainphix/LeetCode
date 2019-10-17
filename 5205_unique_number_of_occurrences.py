class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        dic = {}
        dit = {}
        unique = True
        for i in arr:
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1

        for j in dic.values():
            if dit.get(j) == None:
                dit[j] = 1
            else:
                dit[j] = dit[j] + 1
                unique = False

        return unique

if __name__ == '__main__':
    arr = [1,2,2,3]
    s = Solution()
    print(s.uniqueOccurrences(arr))