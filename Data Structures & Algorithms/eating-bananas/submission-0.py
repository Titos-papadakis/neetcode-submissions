class Solution:

  def minEatingSpeed(self, piles: list[int], h: int) -> int:
    l, r = 1, max(piles)

    while l < r:
      mid = (l + r) // 2
      # sum wrwn 
      hours = sum((p + mid - 1) // mid for p in piles)

      if hours <= h:
        r = mid  # ginetai me mikroteri
      else:
        l = mid + 1  # pigene pio grigora

    return l