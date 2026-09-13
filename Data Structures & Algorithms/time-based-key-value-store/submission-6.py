class TimeMap:

    def __init__(self):
        self.kv_store: defaultdict[str, list[tuple[str, int]]] =  defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        kv_list = self.kv_store.get(key)
        if not kv_list or kv_list[0][1] > timestamp:
            return ""
        l, r = 0, len(kv_list) - 1
        # find max t <= timestamp
        while l < r:
            mid  = (l+r+1) // 2
            if kv_list[mid][1] <= timestamp:
                l = mid
            else:
                r = mid - 1
        return kv_list[l][0]

