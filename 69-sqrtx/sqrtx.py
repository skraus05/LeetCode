class Solution:
    def mySqrt(self, x: int) -> int:
        x = math.sqrt(x)
        roundedDown = math.floor(x)
        return roundedDown