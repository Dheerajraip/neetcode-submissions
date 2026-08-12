class Solution:
    def isPalindrome(self, s: str) -> bool:
        set=""
        t=s.lower()
        for ch in t:
            if ch.isalnum():
                set+=ch
        return set==set[::-1]
        