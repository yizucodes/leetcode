class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0
        left = 0
        n = len(height)
        right = n - 1

        distance = n - 1

        # distance

        while left < right:
        # calculate area
        # smallest of the two heights * distance
            leftH = height[left]
            rightH = height[right]
            currArea = min(leftH, rightH) * distance 

        # compare currentArea vs maxArea
            if currArea > maxArea:
        # if currentArea > maxArea --> maxArea = currentArea
                maxArea = currArea

        # leftH < rightH
        # left += 1
            if leftH <= rightH:
                left += 1
            elif leftH > rightH:
                right -= 1

            # # same
            # else:
                


        # leftH > rightH
        # right += 1

        # if equal height, which pointer to move?
        # move to the next bar which is greater for either left or right

            distance -= 1

        return maxArea
        