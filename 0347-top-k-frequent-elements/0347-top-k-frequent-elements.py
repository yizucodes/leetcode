from collections import Counter 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqMap
        freqMap = Counter(nums)
        minHeap = []

        # create minHeap with tuples (freq, element)
        for el, freq in freqMap.items():
            if len(minHeap) < k:
                # push top of heap
                heapq.heappush(minHeap, (freq, el))
            # elif len(heap) == k and freq of element > freq top element of heap: 
            elif len(minHeap) == k and freq > minHeap[0][0]:
                # push new to min heap only if the freq is higher than the top value
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (freq, el))

        return [tup[1] for tup in minHeap]