from typing import TypedDict, List, Dict

class Entry(TypedDict):
    value: str
    timestamp: int

class TimeMap:

    def __init__(self):
        self.kv: Dict[List[Entry]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.kv.get(key):
            value_pairs: List[Entry] = self.kv[key]
        else:
            value_pairs: List[Entry] = []
        value_pairs.append({
            "value": value,
            "timestamp": timestamp
        })
        self.kv[key] = value_pairs
        
    def get(self, key: str, timestamp: int) -> str:

        value_pairs: List[Entry] = self.kv.get(key, [])
        l, r = 0, len(value_pairs) - 1

        res = ''
        while l <= r:
            mid_index = (l+r) // 2
            mid_ts = value_pairs[mid_index]['timestamp']
            if mid_ts == timestamp:
                return value_pairs[mid_index]['value']
            if mid_ts < timestamp:
                l = mid_index + 1
                res = value_pairs[mid_index]["value"]
            else:
                r = mid_index - 1
        return res