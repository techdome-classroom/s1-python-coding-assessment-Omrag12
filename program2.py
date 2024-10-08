def decode_message( s: str, p: str) -> bool:

# write your code here
   m, n = len(s), len(p)
   dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: Empty string and empty pattern are a match
   dp[0][0] = True
    
    # Handle the case where the pattern contains '*' at the beginning
   for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
   for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                # If current characters match or the pattern has '?', propagate the previous result
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' can match any sequence: we check if skipping '*' or matching it works
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    # The result is whether the entire string matches the entire pattern
    return dp[m][n]
        return False