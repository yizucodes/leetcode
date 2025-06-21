class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A)

        while True:
            i = (l + r) // 2  # Elements taken from A
            j = half - i      # Elements taken from B

            Aleft = A[i-1] if i > 0 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")
            Bleft = B[j-1] if j > 0 else float("-infinity") 
            Bright = B[j] if j < len(B) else float("infinity")

            # check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2  
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1