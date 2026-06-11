class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            temp = nums1+nums2
            temp.sort()

            if len(temp) % 2 == 1:
                return temp[len(temp) // 2]
            else:
                return (temp[int(len(temp) / 2) - 1] + temp[int(len(temp) / 2)]) / 2
