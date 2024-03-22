class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list_set = set(nums)
        answers = []
        for i in range(1, len(nums)+1):
            if i not in list_set:
                answers.append(i)
        return answers