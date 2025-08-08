import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all the non alphanumeric characters
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True


sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))