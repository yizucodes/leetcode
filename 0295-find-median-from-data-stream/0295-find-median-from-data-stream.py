import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = [] # large nums
        self.maxHeap = [] # small nums

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -num)
        elif num <= abs(self.maxHeap[0]):
            # add to max_heap (it's a small number)
            heapq.heappush(self.maxHeap, -num)
        else:
            # add to min_heap (it's a large number)
            heapq.heappush(self.minHeap, num)
        # After adding num to one of the heaps:
        # Case 1: Max heap too big
        if len(self.maxHeap) > len(self.minHeap) + 1:
            # Move top of max to min
            popped = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -popped)

        # Case 2: Min heap too big  
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            # Move top of min to max
            popped = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -popped)

    def findMedian(self) -> float:
        # Total numbers is EVEN:
        # Both heaps have equal size
        if len(self.maxHeap) == len(self.minHeap):
            # Median = average of both tops
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        # Total numbers is ODD:
        else:
            # One heap has more elements (size difference = 1)
            # Median = top of the larger heap
            
            isMinHeapLarger = len(self.minHeap) > len(self.maxHeap)
            if isMinHeapLarger:
                return self.minHeap[0]
            else:
                return -self.maxHeap[0]
      
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()