class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}

        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        
        ans = 0
        for key,value in m.items():
            if value == 1:
                ans = key
        return ans