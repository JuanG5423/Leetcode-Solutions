class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        answer = []
        for number in nums:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1
        for i in range(k):
            most_common = max(counts, key=counts.get)
            answer.append(most_common)
            del counts[most_common]

        return answer