from typing import List
from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        if len(nums) % k != 0:
            return False
        nums = sorted(nums)
        static = Counter(nums)
        for i,j in static.items():
            if static.get(i) != 0:
                for z in range(1, k):
                    if static.get(i+z) != None:
                        if static.get(i+z) != 0:
                            if static[i] > static[i+z]:
                                return False
                            else:
                                static[i+z] -= static[i]
                    else:
                        return False
        return True

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1,2,3,4,3,4,5,9,10,11]
    k = 3
    print(s.isPossibleDivide(nums, k))