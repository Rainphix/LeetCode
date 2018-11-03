# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#
#         len1 = len(l1)
#         len2 = len(l2)
#         inter = []
#
#         if len1 <= len2:
#             l1,l2 = l2,l1
#             len1,len2 = len2,len1
#
#         addi = 0
#
#         for i in range(len2):
#
#             if addi == 1:
#
#                 if (l1[i] + l2[i] + 1) >= 10:
#
#                     inter.append((l1[i] + l2[i] + 1) % 10)
#                     addi = 1
#                 else:
#                     inter.append(l1[i] + l2[i] + 1)
#                     addi = 0
#             else:
#
#                 if (l1[i] + l2[i])  >= 10:
#
#                     inter.append((l1[i] + l2[i]) % 10)
#                     addi = 1
#                     print(addi)
#                 else:
#                     inter.append(l1[i] + l2[i])
#                     addi = 0
#
#         if len1 == len2:
#             if addi == 1:
#                 inter.append(1)
#             return inter
#         else:
#             for i in range(len2,len1):
#
#                 if i == len1:
#                     if addi == 1:
#                         if l1[i] + 1 >= 10:
#                             inter.append((l1[i] + 1) % 10)
#                             addi = 1
#                         else:
#                             inter.append((li[i] + 1) % 10)
#                             addi = 0
#                     else:
#                         inter.append(l1[i] % 10)
#                 else:
#                     if addi == 1:
#                         if l1[i] + 1 >= 10:
#                             inter.append((l1[i] + 1) % 10)
#                             addi = 1
#                         else:
#                             inter.append((l1[i] + 1) % 10)
#                             addi = 0
#                     else:
#                         inter.append(l1[i] % 10)
#             if addi == 1:
#                 inter.append(1)
#
#             return inter
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val_sum = l1.val + l2.val
        list_node = ListNode(val_sum % 10)
        a = val_sum // 10
        node = list_node
        while True:
            try:
                l1 = l1.next
            except:
                pass
            try:
                l2 = l2.next
            except:
                pass
            if not l1 and not l2:
                break
            elif not l1:
                l1_val = 0
                l2_val = l2.val
            elif not l2:
                l2_val = 0
                l1_val = l1.val
            else:
                l1_val = l1.val
                l2_val = l2.val
            val_sum = l1_val + l2_val + a
            temp_node = ListNode(val_sum % 10)
            node.next = temp_node
            node = temp_node
            a = val_sum // 10
        if a != 0:
            node.next = ListNode(a)
        return list_node

if __name__ == '__main__':

    l1 = []
    l2 = []
    S = Solution()
    s = S.addTwoNumbers(l1,l2)
    print(s)
