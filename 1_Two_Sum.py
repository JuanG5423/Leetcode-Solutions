class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, num in enumerate(nums):
            if target-num in indices:
                return [index, indices[target-num]]
            indices[num] = index