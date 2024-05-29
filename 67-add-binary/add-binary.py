class Solution:
    def addBinary(self, a: str, b: str) -> str:
        numberA = int(a, 2)
        numberB = int(b, 2)
        numberSum = numberA + numberB
        return bin(numberSum)[2:]