import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        # value : index (index from self.data)
        self.val_to_idx = {}
        
    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False

        self.data.append(val)
        self.val_to_idx[val] = len(self.data) - 1
        return True
        
    def remove(self, val: int) -> bool:
        # check from dictionary if value exist
        if val not in self.val_to_idx:
            return False

        removeIndex = self.val_to_idx[val]

        # last element of list
        lastElement = self.data[-1]

        # swap
        self.data[removeIndex], self.data[-1] = self.data[-1], self.data[removeIndex]

        # pop last element
        self.data.pop()

        # update dictionary with new index of swapped  --> the swappedItemValue has removeIndex as value
        self.val_to_idx[lastElement] = removeIndex

        # remove deleted value from dictionary
        del self.val_to_idx[val]

        return True

    def getRandom(self) -> int:
        # random index
        randomIndex = random.randint(0, len(self.data) - 1)
        return self.data[randomIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()