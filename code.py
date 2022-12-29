class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(ord(ch)+32*('A'<=ch<='Z')) for ch in s)
