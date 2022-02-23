# maps keys to values for fast lookup
# array of linked lists, and a hash function to map values to the linked lists
#
#  hi    abc    aa    qs     pl
#  3      1      2    2      2
#  
# final hash table:
# [abs] [aa]  [hi]
#       [qs]  
#       [pl]

class HashTable():
    def __init__(self):
        self.table = []
        for i in range(10): self.table.append([])

    def __repr__(self):
        return 'Hash Table: \n' + repr([x for x in self.table])

    def insert(self, key, value):
        idx = self.hash_function(key)
        print(f'appending to slot {idx}')
        self.table[idx].append(value)
        print(f'data inserted: {self.table[idx]}')

    def lookup(self, key):
        return self.table[self.hash_function(key)]
            
    def hash_function(self, key):
        hash_ = key % 9
        print(f'Hash: {hash_}')
        return hash_

ht = HashTable()
print(repr(ht))
ht.insert(1234, 19239376136)
print(ht.lookup(55555))
print(ht.lookup(1234))
print(repr(ht))
