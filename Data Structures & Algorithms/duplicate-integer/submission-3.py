class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for index, num in enumerate(nums):
            if num in hash_table:
                if num in hash_table:
                    return True
            hash_table[num] = index
        return False

        