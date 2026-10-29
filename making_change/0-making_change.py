#!/usr/bin/python3
"""Find the minimum number of coins needed to make change."""


def makeChange(coins, total):
    """Return the fewest coins needed to reach total."""
    if total <= 0:
        return 0

    # dp[amount] stores the fewest coins needed for that amount.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                coins_needed = dp[amount - coin] + 1
                if coins_needed < dp[amount]:
                    dp[amount] = coins_needed

    if dp[total] == float('inf'):
        return -1
    return dp[total]
