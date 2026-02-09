import random

class RandomizedSet:

    def __init__(self):
        self.list = []
        self.valToIndex = {}

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False
        self.list.append(val)
        self.valToIndex[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valToIndex:
            return False

        lastEl = self.list[-1]
        
        indexVal = self.valToIndex[val]
        self.valToIndex[lastEl] = indexVal
        del self.valToIndex[val]
        
        # remove value
        # swap index of last element with val
        self.list[indexVal], self.list[-1] = self.list[-1], self.list[indexVal]
        self.list.pop()
        return True

    def getRandom(self) -> int:
        # random number from 0 to len(list) - 1
        if not self.list:
            return
        randomIndex = random.randint(0, len(self.list) - 1)
        return self.list[randomIndex]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()