class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 1:
            return float(nums1[len(nums1)//2])
        else:
            return float((nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2])/2)


'''
[1, 2, 3] [2, 5] [1, 2, 2, 3, 5]
'''

#Could also use the merging part of merge sort
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        if i < len(nums1):
            merged += nums1[i:]
        elif j < len(nums2):
            merged += nums2[j:]
        return merged[len(merged)//2] if len(merged) % 2 else (merged[len(merged)//2-1] + merged[len(merged)//2])/2