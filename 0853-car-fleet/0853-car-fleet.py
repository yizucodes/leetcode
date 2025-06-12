class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Createcars with position and time to reach target
        cars = []
        for i in range(len(position)):
            timeToTarget = (target - position[i]) / speed[i]
            cars.append([position[i], timeToTarget])

        # Sort cars by position in decreasing order (closes to target first)
        cars.sort(reverse=True)

        stack = []
        
        # Use monotonic stack to track fleet time
        for car in cars:
            currentTime = car[1]

            if len(stack) == 0 or currentTime > stack[-1]:
                stack.append(currentTime)

        
        return len(stack)