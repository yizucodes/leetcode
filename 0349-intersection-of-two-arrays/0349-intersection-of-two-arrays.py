class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # empty arrays 
        # if one empty array return []

        # set1 and set 2
        set1 = set(nums1)
        set2 = set(nums2)

        # return intersection
        return list(set1 & set2)