class MyHashSet:

    def __init__(self):
        self.cap = 10**4
        self.buckets = [[] for _ in range(self.cap)]
        self.size = 0
        self.load_factor_threshold = 0.75

    def _hash(self, key: int) -> int:
        if isinstance(key, (int, float)):
            return int(key) % self.cap
        elif isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (h * 31) + ord(char)
            return hash_value % self.cap
        else:
            rep = str(key)
            hash_value = 0
            for char in key:
                hash_value = (h * 131) + ord(char)
            return hash_value % self.cap

    def _resize(self):
        old_bucket = self.buckets
        self.cap *= 2
        self.size = 0
        self.buckets = [[] for _ in self.cap]

        for bucket in buckets:
            for key in bucket:
                self.add(key)           

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]

        for item in bucket:
            if item == key:
                return
        bucket.append(key)
        self.size += 1
        return

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]

        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                self.size -= 1
                return
        return None

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]

        for item in bucket:
            if item == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)