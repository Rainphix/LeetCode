

# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """
#         MAX_INT=0x7fffffff
#         if divisor==0: return MAX_INT
#         sign=1
#         if divisor<0:
#             sign=-sign
#             divisor=-divisor
#         if dividend<0:
#             sign=-sign
#             dividend=-dividend
#         res=0
#         while  dividend>=divisor:
#             redu=divisor
#             res0=1
#             while dividend>redu*2:
#                 res0<<=1
#                 redu<<=1
#             dividend-=redu
#             res+=res0
#         if sign<0:
#             res=-res
#         if res>MAX_INT:
#             res=MAX_INT
#         return res

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """



if __name__ == '__main__':
    s = Solution()
    ans = s.divide(-2147483648,2)
    print(ans)
    exit()
