class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            temp = []

            for i in range(len(nums1)):
                temp.append(nums1[i])
            for i in range(len(nums2)):
                temp.append(nums2[i])

            temp.sort()

            if len(temp) % 2 == 1:
                return temp[len(temp) // 2]
            else:
                return (temp[int(len(temp) / 2) - 1] + temp[int(len(temp) / 2)]) / 2
