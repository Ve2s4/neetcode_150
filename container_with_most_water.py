from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l,r = 0, len(height) -1
        ans = 0

        while l != r:
            lc = height[l]
            rc = height[r]
            vol = (r-l) * min(lc, rc)

            ans = max(ans, vol)

            if lc <= rc:
                l += 1
            else:
                r -= 1
        
        return ans
    

sol = Solution()

print(sol.maxArea([1,8,6,2,5,4,8,3,7]))