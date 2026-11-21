class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = set()
        for x in nums:
            if x in hash_table:
                return True
            hash_table.add(x)
        return False