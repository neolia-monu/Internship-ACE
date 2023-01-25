class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        res = strs[0]
        if len(strs) == 1:
            return res

        for i in range(1, len(strs)):
            min_val = min(res, strs[i])
        
            in_str = ""

            for j in range(0, len(min_val)):

                if res[j] == strs[i][j]:
                    in_str = in_str + res[j]
                else:
                    break

            res = in_str
        
        return res