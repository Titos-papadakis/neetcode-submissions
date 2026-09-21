class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()#gia na einai diadoxika ta merges
    arr=[intervals[0]]#arxikopoiisi toy pinaka
    for i in intervals[1:]:#ap to 2o stoixeio
      if arr[-1][1]>=i[0]:#an ayto poy einai ston pinaka me ta merges einai megalytero apo ayto poy eimaste twra
        arr[-1][1]=max(arr[-1][1],i[1])#pare to megalytero ap to end_i
      else:
        arr.append(i)#an einai ksexwristo valto ston pinaka mono toy
    return arr
    