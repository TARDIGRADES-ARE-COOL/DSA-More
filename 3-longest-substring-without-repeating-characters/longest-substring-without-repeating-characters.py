class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        max_len = 0 

        for c in s:
            while c in temp:
                temp.pop(0)
            temp.append(c)
            max_len = max(max_len, len(temp))
        return max_len
        