class Solution:
    def mySqrt(self, x: int) -> int:
        x = x ** 0.5
        roundedDown = math.floor(x)
        return roundedDown