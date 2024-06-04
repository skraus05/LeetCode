class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Step 1: Count occurrences of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Step 2: Calculate the length of the longest palindrome
        length = 0
        odd_found = False
        
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        # Step 3: If there was an odd count, add one to the length
        if odd_found:
            length += 1
        
        return length
