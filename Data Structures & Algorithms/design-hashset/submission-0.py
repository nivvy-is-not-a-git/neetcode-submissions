class MyHashSet:

    def __init__(self):
        self.hash=[]
        for i in range(1000):
            self.hash.append([])

    def _hash(self, key: int) -> int:
        return key % 1000

    def add(self, key: int) -> None:
        if self.contains(key)==False:
            self.idx = self._hash(key)
            self.hash[self.idx].append(key)

    def remove(self, key: int) -> None:
        self.idx = self._hash(key)
        if self.contains(key) == True:
            self.hash[self.idx].remove(key)


    def contains(self, key: int) -> bool:
        self.idx = self._hash(key)
        for i in range(len(self.hash[self.idx])):
            if self.hash[self.idx][i] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)