class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

if __name__ == '__main__':

    list1 = [1,23,46,89,12156,1256,15648,364,8945,364,455]
    list2 = [2,6,87,45,4545,15145,48545,115,96,489,41,411,1516,889565,11,6548949464]
    print(sorted(list1),sorted(list2))
    print(len(list1),len(list2))

    m = len(list1)
    n = len(list2)

    if m < n:

        list1,list2 = list2,list1
