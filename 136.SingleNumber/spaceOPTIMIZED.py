class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR all numbers
        return result



# Why XOR Works
# XOR has properties that make it perfect for this problem:
# 𝑥 ⊕ 𝑥 = 0
# x⊕x=0 (a number XOR-ed with itself cancels out).
# 𝑥 ⊕ 0 = 𝑥
# x ⊕ 0= x.
# XOR is commutative and associative, so the order doesn't matter.
# Using XOR, pairs of duplicate numbers cancel each other, leaving only the single number.