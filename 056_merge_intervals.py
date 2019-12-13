class Solution:
    def merge(self, intervals):

        if not intervals:
            return []
        merged = []
        l, r = 0, 0
        cur = 0
        intervals=sorted(intervals)

        while(cur < len(intervals)-1):

            l = intervals[cur][-1]
            r = intervals[cur+1][0]

            if l >= r:
                intervals[cur+1][0] = intervals[cur][0]
                if intervals[cur+1][-1] < intervals[cur][-1]:
                    intervals[cur + 1][-1] = intervals[cur][-1]
            else:
                merged.append(intervals[cur])
            cur += 1

        merged.append(intervals[-1])
        return merged

if __name__ == '__main__':
    s = Solution()
    # intervals = [[1,9],[2,11],[3,19],[4,15],[9,10]]
    intervals = [[1,4],[0,4]]
    ans = s.merge(intervals)
    print(ans)