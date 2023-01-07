class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for price in costs:
            coins -= price
            if coins >= 0: 
                count += 1
            else:
                break
        return count

