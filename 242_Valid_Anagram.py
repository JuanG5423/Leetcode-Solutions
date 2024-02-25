class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1 = {}
        counts2 = {}
        for char in s:
            if char in counts1:
                counts1[char] += 1
            else:
                counts1[char] = 1
        for char in t:
            if char in counts2:
                counts2[char] += 1
            else:
                counts2[char] = 1
        return True if counts1 == counts2 else False