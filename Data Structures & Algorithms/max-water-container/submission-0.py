class Solution:
    def maxArea(self, heights: List[int]) -> int:
    #etsi opws to blepw prepei na parw ta 2 akra    
    #na ypologisw to width right-left kai to height me to min height twn 2 
    #kai na pigainw pros ti mesi kai stamataw mexri left=right 
    #kai tha pairnw kathe fora ayto poy einai mikrotero ap ta diplana
        mcounter=-1
        maxw=0
        width=len(heights)-1
        i=0
        while width>0 :
            height=min(heights[i],heights[mcounter])
            if heights[i]<heights[mcounter]:
                i=i+1
            else:
                mcounter=mcounter-1
            maxw=max(maxw,height*width)
            width=width -1
        
        return maxw