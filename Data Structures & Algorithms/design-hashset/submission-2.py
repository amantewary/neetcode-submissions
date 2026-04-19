class MyHashSet:
    def __init__(self):
        self.cap = 8  # Start with a small capacity
        self.buckets = [[] for _ in range(self.cap)]
        self.size = 0
        self.load_factor_threshold = 0.75

    def _hash(self, key) -> int:
        return hash(key) % self.cap

    def _resize(self):
        old_buckets = self.buckets
        self.cap *= 2
        self.buckets = [[] for _ in range(self.cap)]
        self.size = 0

        for bucket in old_buckets:
            for key in bucket:
                self.add(key)

    def add(self, key) -> None:
        if self.size >= self.cap * self.load_factor_threshold:
            self._resize()
        bucket = self.buckets[self._hash(key)]

        if key not in bucket:  # Avoid duplicates
            bucket.append(key)
            self.size += 1

    def remove(self, key) -> None:
        bucket = self.buckets[self._hash(key)]

        if key in bucket:
            bucket.remove(key)
            self.size -= 1

    def contains(self, key) -> bool:
        bucket = self.buckets[self._hash(key)]
        return key in bucket
    
    def __len__(self):
        return self.size