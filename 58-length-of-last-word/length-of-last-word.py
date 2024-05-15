class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:
            return 0
        last_word = words[-1]
        return len(last_word)