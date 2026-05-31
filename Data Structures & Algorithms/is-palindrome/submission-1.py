class Solution:
    def isPalindrome(self, s: str) -> bool:
        set=""
        for ch in s:
            if ch.isalnum():
                set+=ch.lower()
        return set==set[::-1]
        