class Solution:
    def span(self, idx, s, n):
        # odd
        odd_left = idx - 1
        odd_right = idx + 1
        while odd_left >= 0 and odd_right <= n-1 and s[odd_left] == s[odd_right]:
            odd_left -= 1
            odd_right += 1
        odd_len = odd_right-1 - (odd_left+1) +1

        # even 
        even_left = idx
        even_right = idx + 1
        while even_left >= 0 and even_right <= n-1 and s[even_left] == s[even_right]:
            even_left -= 1
            even_right += 1
        even_len = even_right-1 - (even_left+1)  + 1
        
        max_len, candidate = None, None
        if even_len >= odd_len:
            max_len, candidate = even_len, s[even_left+1:even_right]
        else:
            max_len, candidate = odd_len, s[odd_left+1:odd_right]

        return max_len, candidate

    def longestPalindrome(self, s: str) -> str:
        ans_len = 1
        ans = s[0]
        n = len(s)
        for i in range(0, n):
            max_len, candidate = self.span(i, s, n)
            if max_len > ans_len:
                ans_len = max_len
                ans = candidate
        return ans