class LRUCache:
    def __init__(self, capacity):
        # Complete this function
        pass
    
    def get(self, key):
        # Complete this function
        pass
    
    def put(self, key, value):
        # Complete this function
        pass

# Test cases
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Expected output: 1
cache.put(3, 3)  # Evicts key 2
print(cache.get(2))  # Expected output: -1
cache.put(4, 4)  # Evicts key 1
print(cache.get(1))  # Expected output: -1
print(cache.get(3))  # Expected output: 3
print(cache.get(4))  # Expected output: 4
