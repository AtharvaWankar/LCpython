class Solution:
    def maxScore(self, s: str) -> int:
        def left_sum(str):
            l_res = 0
            for i in str:
                if i == '0':
                    l_res += 1
            return l_res
    
        def right_sum(str):
            r_res = 0
            for i in str:
                if i == '1':
                    r_res += 1
            return r_res
    
        ans = []
            
        for i in range(1,len(s)):
            
            # print((s[:i]), " ", (s[i:]))
            
            ans.append(left_sum(s[:i]) + right_sum(s[i:]))
            
        val = max(ans)
        return val