class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count_s = {}
        char_count_t = {}
        for c in s:
            if c not in char_count_s:
                char_count_s[c] = 1
            char_count_s[c]+=1
        for c in t:
            if c not in char_count_t:
                char_count_t[c] = 1
            char_count_t[c]+=1
        if char_count_s == char_count_t:
            return True
        return False
        