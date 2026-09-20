class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        max_sub=0
        left=0
        for right in s:
            while right in char_set:
                char_set.remove(s[left])
                left=left+1
            char_set.add(right)

            max_sub=max(max_sub,len(char_set))
        return max_sub