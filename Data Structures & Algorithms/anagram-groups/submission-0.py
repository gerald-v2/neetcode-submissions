class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #HASH MAPS METHOD
        hash_maps = {}
        for words in strs:
            key = ''.join(sorted(words))
            if key not in hash_maps:
                hash_maps[key] = []
            hash_maps[key].append(words)
        return list(hash_maps.values())
        