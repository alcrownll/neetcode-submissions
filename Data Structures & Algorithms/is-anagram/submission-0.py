class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_char = {}

        for char in s:
            seen_char[char] = seen_char.get(char, 0) + 1

        for char in t:
            if char not in seen_char:
                return False
            seen_char[char] -= 1
            if seen_char[char] < 0:
                return False

        return True

        