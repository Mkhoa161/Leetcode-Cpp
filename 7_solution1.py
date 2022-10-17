class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        num = abs(x)
        while num != 0:
            reverse = reverse*10 + num%10
            num //= 10
        if x < 0:
            reverse *= -1
        if -2**31 > reverse or reverse > 2**31-1:
            return 0
        return reverse
