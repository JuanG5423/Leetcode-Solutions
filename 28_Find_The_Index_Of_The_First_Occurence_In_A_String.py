class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for index, char in enumerate(haystack):
            if char == needle[0]:
                count = 0
                possible = haystack[index:]
                for i in range(min(len(needle), len(possible))):
                    if possible[i] == needle[i]:
                        count += 1
                if count == len(needle):
                    return index
        return -1