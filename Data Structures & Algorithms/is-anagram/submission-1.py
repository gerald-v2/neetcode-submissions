class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_maps = {}
        if len(s) != len(t):
            return False
        for x in s:
            if x not in hash_maps:
                hash_maps[x] = 0
            hash_maps[x] += 1
        for a in t:
            if a not in hash_maps or hash_maps[a] == 0:
                return False
            hash_maps[a] -= 1
        return True
            