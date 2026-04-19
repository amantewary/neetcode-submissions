class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for c in s:
            if c not in count_s:
                count_s[c] = 1
            count_s[c]+=1
        for c in t:
            if c not in count_t:
                count_t[c] = 1
            count_t[c]+=1
        return count_s == count_t
        