class Solution:
    def isValid(self, s: str) -> bool:
        #oso einai {[( kanw append se stoiva oso einai }]) kanw pop an einai adeia einai valid alliws oxi 
        arr=[]
        for i in s:
            if i =="{" or i=="[" or i=="(":
                arr.append(i)
            elif len(arr)!=0:   
                if i=="}" and arr[-1]=="{":
                    arr.pop()
                elif  i=="]" and arr[-1]=="[":
                    arr.pop()
                elif i==")"and arr[-1]=="(":
                    arr.pop()  
                else:
                    return False   
            else:
                return False      
        if len(arr)==0:
            return True
        else:
            return False