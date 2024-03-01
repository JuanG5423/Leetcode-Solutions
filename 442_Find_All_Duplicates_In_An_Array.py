class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        empty_set = set([])
        duplicate_set = set([])
        for num in nums:
            if num in empty_set:
                duplicate_set.add(num)
            empty_set.add(num)
        return duplicate_set