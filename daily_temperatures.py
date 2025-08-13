from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)

        stack: List[tuple[int, int]] = [] # [(index, temp)]

        for index, ele in enumerate(temperatures):
            while stack and stack[-1][1] <= ele:
                temp_index, _ = stack.pop()
                ans[temp_index] = index - temp_index
            stack.append((index, ele))

        return ans
    
sol = Solution()

print(sol.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))