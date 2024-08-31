def hash(self, key):
  key_bytes = key.encode()
  hash_code = sum(key_bytes)
  return hash_code

def compressor(self, hash_code):
  return hash_code % self.array_size

def assign(self, key, value):
  array_index = self.compressor(self.hash(key))
  self.array[array_index] = [key, value]