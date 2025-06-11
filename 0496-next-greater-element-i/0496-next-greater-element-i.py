class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        res = []

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                # map number to 1
                # index of nums1 of number of nums2
                next_greater[smaller] = num
            stack.append(num)

        for num in nums1:
            res.append(next_greater.get(num, -1))


        return res
        