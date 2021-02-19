class Solution:
    def numDecodings(self, s: str) -> int:
        decode_dict = {}
        for i in range(1, 27):
            decode_dict[str(i)] = i
        
        N = len(s)
        dp = [int(s[0] in decode_dict)] * N
        if N > 1: 
            for i in range(1, N):
                if s[(i - 1):(i + 1)] in decode_dict and s[i] in decode_dict:
                    if s[i] == '0':
                        dp[i] == dp[i - 2]    
                    else:
                        dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = dp[i - 1]
        print(dp)
        return dp[-1] 