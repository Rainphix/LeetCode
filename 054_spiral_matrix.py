# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         # 取首行，去除首行后，对矩阵翻转来创建新的矩阵，
#         # 再递归直到新矩阵为[],退出并将取到的数据返回
#         ret = []
#         if matrix == []:
#             return ret
#         ret.extend(matrix[0]) # 上侧
#         new = [reversed(i) for i in matrix[1:]]
#         if new == []:
#             return ret
#         r = self.spiralOrder([i for i in zip(*new)])
#         ret.extend(r)
#         return ret

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        up,down,left,right = 0,len(matrix),0,len(matrix[0])  #边界条件
        res = []
        while left < right or up < down:
            for i in range(left,right):  ##先向右
                res.append(matrix[up][i])
            if up+1 >= down:             #是否超出边界
                break
            else:
                up += 1
            for i in range(up,down):     #再向下
                res.append(matrix[i][right-1])
            if right-1<=left:           #是否超出边界
                break
            else:
                right -= 1
            for i in range(right-1,left-1,-1): #再向左
                res.append(matrix[down-1][i])
            if down-1<=up:               #是否超出边界
                break
            else:
                down -= 1
            for i in range(down-1,up-1,-1):  #再向上
                res.append(matrix[i][left])  #是否超出边界
            if left+1>=right:
                break
            else:
                left += 1
        return res

if __name__ == '__main__':

    s = Solution()
    matrix = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]]
    ans = s.spiralOrder(matrix)
    print(ans)