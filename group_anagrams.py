from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = {}

        for string in strs:
            
            key = "".join(sorted(string))

            if output.get(key):
                output[key] = output[key] +[string]
            else:
                output[key] = [string]

        return list(output.values())