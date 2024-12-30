import random


class RandomizedSet:
    def __init__(self):
        self._list = list()
        self._dict = dict()

    def insert(self, val: int) -> bool:
        if val in self._dict:
            return False
        else:
            self._list.append(val)
            self._dict[val] = len(self._list) - 1
            return True

    def remove(self, val: int) -> bool:
        try:
            index = self._dict.pop(val)
        except KeyError:
            return False

        end_val = self._list.pop()

        if index != len(self._list):
            self._list[index] = end_val
            self._dict[end_val] = index

        return True

    def getRandom(self) -> int:
        return random.choice(self._list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

