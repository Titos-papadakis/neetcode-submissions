class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chr_set=set()
        left=0
        maxsub=0
        for right in s:
            while right in chr_set:
                chr_set.remove(s[left])
                left=left+1
            chr_set.add(right)
            
            maxsub=max(len(chr_set),maxsub)
        return maxsub