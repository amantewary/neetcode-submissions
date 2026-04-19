class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_before = {}
        for n in nums:
            if n in seen_before.keys():
                return True
            seen_before[n] = True
        return False