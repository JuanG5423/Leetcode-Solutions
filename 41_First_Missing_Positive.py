class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if (nums[0] > 1 or nums[0] <= 0) else nums[0]+1
        positive_set = set([])
        for num in nums:
            if num > 0:
                positive_set.add(num)
        if len(positive_set) == 0:
            return 1
        if min(nums) > 1 or (min(nums) < 1 and 1 not in positive_set):
            return 1
        else:
            for i in range(min(positive_set), max(positive_set)):
                if i not in positive_set:
                    return i
            return max(positive_set) + 1