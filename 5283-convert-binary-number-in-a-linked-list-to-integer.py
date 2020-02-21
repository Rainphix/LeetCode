# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head):

        if not head:
            return 0
        tail = []

        head = list(head)

        for i in head:
            tail.append(str(i))

        two = ''.join(tail)
        two = '0b' + two
        return int(two,2)


if __name__ == '__main__':
    s = Solution()
    head = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    print(s.getDecimalValue(head))