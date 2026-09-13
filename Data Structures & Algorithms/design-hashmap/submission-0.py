class MyHashMap:

    def __init__(self):
        self.hash = []
        for i in range(1000):
            self.hash.append([])

    def _hash(self, key: int) -> int:
        return key % 1000

    def _search(self, key: int) -> int:
        self.idx = self._hash(key)
        for i in range(len(self.hash[self.idx])):
            if self.hash[self.idx][i][0]==key:
                return i
        return -1
        
    def put(self, key: int, value: int) -> None:
        self.idx = self._hash(key) 
        index = self._search(key)
        if index == -1:
            self.hash[self.idx].append((key, value))
        else:
            self.hash[self.idx][index] = (key, value)

    def get(self, key: int) -> int:
        index = self._search(key)
        if index != -1:
            self.idx = self._hash(key)
            return self.hash[self.idx][index][1]
        else:
            return -1


    def remove(self, key: int) -> None:
        self.idx = self._hash(key)
        index = self._search(key)
        if index!=-1:
            for i in range(len(self.hash[self.idx])):
                if self.hash[self.idx][i][0]==key:
                    self.hash[self.idx].pop(i)
                    break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)