class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key, [])
        if not arr: 
            return ""
        ans = ""
        for t,v in arr:
            if t <= timestamp:
                ans = v
            else:
                break
        return ans
        