class HashTable:
    def __init__(self, length=4096):
        self.MAX_HASH_TABLE_SIZE = length # cREATE A LIST OF A FIXED SIZE
        self.data_list = [None] * self.MAX_HASH_TABLE_SIZE

    def get_index(self, key):
        result = 0
        for ch in key:
            result += ord(ch)

        return result % self.MAX_HASH_TABLE_SIZE

    def insert(self, key, value):
        ind = self.get_index(key)
        self.data_list[ind] = (key, value)

    def find(self, key):
        ind = self.get_index(key)
        if not self.data_list[ind]:
            return None

        return self.data_list[ind][1]

    def update(self, key, value):
        ind = self.get_index(key)
        self.data_list[ind] = (key, value)

    def print(self):
        keys = [kv[0] for kv in self.data_list if kv is not None]
        return keys