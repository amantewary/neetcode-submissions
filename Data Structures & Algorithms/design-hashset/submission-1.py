class MyHashSet:
    def __init__(self, initial_cap=1024, load_factor=0.75):
        self.cap = initial_cap
        self.load = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(self.cap)]

    def _index(self, key):
        return (key * 2654435761) & 0xFFFFFFFF % self.cap  # simple mix

    def _resize(self):
        old = self.buckets
        self.cap *= 2
        self.buckets = [[] for _ in range(self.cap)]
        for bucket in old:
            for k in bucket:
                self.buckets[self._index(k)].append(k)

    def add(self, key):
        if (self.size + 1) > self.cap * self.load:
            self._resize()
        b = self.buckets[self._index(key)]
        for v in b:
            if v == key:
                return
        b.append(key)
        self.size += 1

    def remove(self, key):
        b = self.buckets[self._index(key)]
        for i, v in enumerate(b):
            if v == key:
                b.pop(i)
                self.size -= 1
                return

    def contains(self, key):
        b = self.buckets[self._index(key)]
        for v in b:
            if v == key:
                return True
        return False
