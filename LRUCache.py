from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.dict = OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dict:
            return -1
        value = self.dict.pop(key)
        self.dict[key] = value
        return value

    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last=False)
        self.dict[key] = value


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put("a", "123")
    cache.put("b", "456")
    cache.put("c", "123")

    # a is not in the cache.
    assert cache.get("a") == -1

    # b is at the front of this ordered dict.
    assert cache.dict.popitem(last=False) == ("b", "456")
    cache.remain += 1

    # c is at the end of this ordered dict.
    cache.put("a", "123")
    cache.put("c", "456")
    assert cache.dict.popitem(last=True) == ("c", "456")
