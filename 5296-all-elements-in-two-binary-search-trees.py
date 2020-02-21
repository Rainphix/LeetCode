# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        trees = []
        self.preTraverse(root1, trees)
        self.preTraverse(root2, trees)
        return sorted(trees)

    def preTraverse(self, root, trees):
        if root == None:
            return
        print(root.val)
        trees.append(root.val)
        self.preTraverse(root.left)
        self.preTraverse(root.right)

if __name__ == '__main__':
    s = Solution()
    root1 = [2, 1, 4]
    root2 = [1, 0, 3]
    print(s.getAllElements(root1, root2))