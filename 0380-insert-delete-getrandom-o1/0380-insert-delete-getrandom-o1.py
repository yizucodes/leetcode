import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        # val: ind
        self.map = {}

    def insert(self, val: int) -> bool:
        # if present return False
        if val in self.map:
            return False

        # insert into list
        self.data.append(val)

        # add value to map
        self.map[val] = len(self.data) - 1

        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        ind = self.map[val]

        self.map[self.data[-1]] = ind 

        # swap to end for value to remove
        self.data[-1], self.data[ind] = self.data[ind], self.data[-1]

        # pop
        self.data.pop()

        # delete from map
        del self.map[val]
        return True

    def getRandom(self) -> int:
        # random index
        randInd = random.randint(0, len(self.data) - 1)
        return self.data[randInd]
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()