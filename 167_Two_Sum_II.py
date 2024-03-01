class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = {}
        answer = []
        for index, num in enumerate(numbers):
            if target-num in indices:
                answer = [index+1, indices[target-num]+1]
                answer.sort()
                return answer
            indices[num] = index
