from bitarray import bitarray
import mmh3


class BloomFilter:
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            index = mmh3.hash(s, seed) % self.size
            self.bit_array[index] = 1

    def find(self, s):
        for seed in range(self.hash_num):
            index = mmh3.hash(s, seed) % self.size
            if self.bit_array[index] == 0:
                return "None"
        return "Probably"


if __name__ == "__main__":
    bf = BloomFilter(10000, 7)
    bf.add("a")
    bf.add("b")
    assert bf.find("a") == "Probably"
    assert bf.find("b") == "Probably"
    assert bf.find("c") == "None"
