class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for number in nums:
            if number not in hash_map:
                hash_map[number] = 0
            hash_map[number] += 1
        sorted_map = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))
        array = []
        for x in range(k):
            array.append(list(sorted_map.keys())[x])
        return array