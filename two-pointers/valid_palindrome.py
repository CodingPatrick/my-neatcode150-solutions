class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_char = ""
        for char in s:
            if char.isalnum():
                only_char = only_char + char.lower()

        return only_char == only_char[::-1]