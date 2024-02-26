#Horrible solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengths = []
        char_counts = {}
        start = -1
        while start < len(s):
            count = 0
            start += 1
            char_counts.clear()
            for index, char in enumerate(s[start:]):
                try:
                    char_counts[char] += 1
                except KeyError:
                    char_counts[char] = 1
                if 2 in char_counts.values():
                    lengths.append(count)
                    break
                if index == len(s)-1-start:
                    lengths.append(count+1)
                    break
                count += 1
                
        return max(lengths) if lengths else 0