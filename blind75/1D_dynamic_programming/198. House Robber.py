# House Robber
def rob(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    # dp[i] represents the maximum amount of money that can be robbed from the first i houses
    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    
    for i in range(2, len(houses)):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])
    
    return dp[-1]