class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                popped_num = stack.pop()
                next_greater[popped_num] = num
            stack.append(num)
        
        # Populate answer
        for i in range(len(nums1)):
            ans.append(next_greater.get(nums1[i], -1))

        return ans
        