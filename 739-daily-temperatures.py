from typing import List

# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         ans = []
#         sub = [0] * len(T)
#         for i in range(1, len(T)):
#             sub[i] = (T[i] - T[i-1])
#         sub.pop(0)
#         sub.append(-float('inf'))
#
#         for j in range(len(sub)):
#             windows = 0
#             windows += sub[j]
#             if windows > 0:
#                 ans.append(1)
#             else:
#                 pos = 0
#                 end = False
#                 while windows <= 0:
#                     pos += 1
#                     if j+pos < len(T):
#                         windows += sub[j+pos]
#                     else:
#                         ans.append(0)
#                         end = True
#                         break
#                 if end == False:
#                     ans.append(pos+1)
#         return ans

class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

if __name__ == '__main__':
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(temperatures))