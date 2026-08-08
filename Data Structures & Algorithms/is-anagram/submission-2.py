class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seed1={}
        seed2={}
        for i in s:
            if i in seed1:
                seed1[i]+=1
            else :    
                seed1[i]=1
        
        for j in t:
            if j in seed2:
                seed2[j]+=1
            else :    
                seed2[j]=1

        return seed1==seed2