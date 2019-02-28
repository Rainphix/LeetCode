class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 每次对target判断，target小于当前i的值时退出
        # 用i连接
        candidates.sort()
        Solution.anslist = []
        self.recursion(candidates,target,0,[])
        return Solution.anslist
    def recursion(self,candidates,target,start,valuelist):
        if target == 0:
            return Solution.anslist.append(valuelist)
        for i in range(start,len(candidates)):
            if candidates[i] > target:
                return
            self.recursion(candidates,target-candidates[i],i,valuelist + [candidates[i]])
        return True

if __name__ == '__main__':

    s = Solution()
    ans = s.combinationSum([1,2,3],5)
    print(ans)
