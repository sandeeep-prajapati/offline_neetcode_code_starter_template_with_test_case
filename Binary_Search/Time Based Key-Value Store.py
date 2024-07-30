from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
    
    def set(self, key, value, timestamp):
        # Complete this function
        pass
    
    def get(self, key, timestamp):
        # Complete this function
        pass

# Test cases
tm = TimeMap()
tm.set("foo", "bar", 1)
print(tm.get("foo", 1))  # Expected output: "bar"
print(tm.get("foo", 3))  # Expected output: "bar"
tm.set("foo", "baz", 4)
print(tm.get("foo", 4))  # Expected output: "baz"
print(tm.get("foo", 5))  # Expected output: "baz"
