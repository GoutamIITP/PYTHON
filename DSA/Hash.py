class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]



    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t.get_hash('march 6')

t['march 6'] = 120

print(t.arr)