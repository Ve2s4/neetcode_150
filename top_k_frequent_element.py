from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Convert them to list of key value pair tuples, [(1, 3), (2, 2), (3, 1)]
        kv_tuples_list = frequency.items()

        # sort them based the second element of each tuple, i.e index 1
        sorted_kv_list = sorted(kv_tuples_list, key=lambda x: x[1], reverse=True)

        # convert them back to the dict and return the first k elements
        return [ele[0] for ele in sorted_kv_list[:k]]
