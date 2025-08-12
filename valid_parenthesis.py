class Solution:
    def isValid(self, s: str) -> bool:

        bracket_stack = []

        opening_pair = ["[", "{", "("]
        closing_pair = ["]","}",")"]

        for index, ele in enumerate(s):
            if ele in opening_pair:
                bracket_stack.append(ele)
            elif ele in closing_pair and bracket_stack:
                last_ele = bracket_stack[-1]
                match last_ele:
                    case "{":
                        if ele == "}":
                            bracket_stack.pop()
                        else:
                            return False
                    case "[":
                        if ele == "]":
                            bracket_stack.pop()
                        else:
                            return False
                    case "(":
                        if ele == ")":
                            bracket_stack.pop()
                        else:
                            return False
            else:
                return False
        return True if not bracket_stack else False


sol = Solution()

print(sol.isValid("(])"))