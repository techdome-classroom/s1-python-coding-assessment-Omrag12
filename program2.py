def decode_message( s: str, p: str) -> bool:

# write your code here
   a, b = len(s), len(p)
   dp = [[False] * (b + 1) for _ in range(a + 1)]

   dp[0][0] = True
    
   for j in range(1, b + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

   for i in range(1, a + 1):
        for j in range(1, b + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
   return dp[a][b]