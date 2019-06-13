import random
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = list()
        self.pos = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        self.num.append(val)
        self.pos[val] = len(self.num) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last_val = self.num[-1]
        self.pos[last_val] = idx
        self.num[idx] = last_val
        self.num.pop(-1)
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.num[random.randint(0, len(self.num) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()