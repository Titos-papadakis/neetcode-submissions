from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
#θελουμε να βαλουμε ολα τα στοιχεια σε ενα      χασμαπ και μετα να χρησιμοποιησουμε την counts-counter
        #και να τυπωσουμε μετα τις 2 πρωτες λιστες
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        sorted_items = sorted(
            res.items(),
            key=lambda pair: pair[1],
            reverse=True
        )

        return [pair[0] for pair in sorted_items[:k]]