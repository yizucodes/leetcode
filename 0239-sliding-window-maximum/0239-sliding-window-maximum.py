from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        deq = deque()
        res = []

        for i in range(len(nums)):
            # Remove indices outside current window

            while deq and deq[0] <= (i - k):
                deq.popleft()
            
            # Remove indices of smaller elements from back
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            # If have full window, record max

            if i >= k-1:
                maximum = nums[deq[0]]
                res.append(maximum)


        return res

"""
SETUP:
- deque = empty (stores indices, not values)
- result = empty array
- window_size = k

FOR each index i from 0 to length-1:

    STEP 1: Remove indices that are outside current window
    WHILE deque is not empty AND front_index <= (i - k):
        remove from front of deque
    
    STEP 2: Remove indices of smaller elements from back
    WHILE deque is not empty AND nums[back_index] < nums[i]:
        remove from back of deque
    
    STEP 3: Add current index to back
    add i to back of deque
    
    STEP 4: If we have a full window, record the maximum
    IF i >= k-1:  // we have at least k elements
        maximum = nums[front_of_deque]
        add maximum to result

RETURN result
"""