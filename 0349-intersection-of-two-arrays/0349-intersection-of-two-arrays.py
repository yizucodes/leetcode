class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []
        shorterList = []
        longerList = []
        # pick shorter array
        if (len(nums1) >= len(nums2)):
            shorterList = nums1
            longerList = nums2
        else:
            shorterList = nums2
            longerList = nums1
        
        # traverse shorter list
        for num in shorterList:
            # if number in longer array, push to result
            if num in longerList and num not in res:
                res.append(num)

        return res
