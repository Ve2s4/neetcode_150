from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, ele in enumerate(nums):
            diff = target - ele
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[ele] = i

solution = Solution()

res = solution.twoSum([3,3], 6)
print(res)