class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 每次对target判断，target小于当前i的值时退出
        # 与39相比，每次i不会停留，每运行一次函数，i+1
        # 在最后添加一个去重函数
        # 战胜31.20%的提交记录 -_-||

        candidates.sort()
        Solution.anslist = []
        self.recursion(candidates,target,0,[])
        Solution.anslist = self.delete_repeat(Solution.anslist)
        return Solution.anslist
    def recursion(self,candidates,target,start,valuelist):
        if target == 0:
            return Solution.anslist.append(valuelist)
        for i in range(start,len(candidates)):
            if candidates[i] > target:
                return
            self.recursion(candidates,target-candidates[i],i+1,valuelist + [candidates[i]])
        return True

    def delete_repeat(self,list):
        l = []
        for i in list:
            if i not in l:
                l.append(i)
            else:
                pass
        return l


class Solution_dalao: # 截的大佬的
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []

        path = []
        res = []
        candidates.sort()

        self.dfs(candidates, path, target, res, 0)
        return res

    def dfs(self, candidates, path, gap, res, start):
        if gap == 0:
            res.append(path)
            return

        previous = -1
        for i in range(start, len(candidates)):
            if previous == candidates[i]:
                continue

            if gap < candidates[i]:
                return

            previous = candidates[i]
            path.append(candidates[i])
            self.dfs(candidates, path.copy(), gap - candidates[i], res, i + 1)
            path.pop()

if __name__ == '__main__':

    s = Solution()
    ans = s.combinationSum2([10,1,2,7,6,1,5],8)
    # ansl = s.delete_repeat([1,1,2,3,5,6,33,1])
    print(ans)
