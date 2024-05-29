class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k, p = 0, 0
        while k < len(s) and p < len(t):
            if s[k] == t[p]:
                k += 1
            p += 1
        return k == len(s)
