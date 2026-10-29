#!/usr/bin/python3
"""Find the minimum number of coins needed to make change."""


def makechange(coins, total):
    """Determine the fewest number of coins needed to make change."""
    if total <= 0:
        return 0

    usable_coins = {coin for coin in coins if 0 < coin <= total}
    if not usable_coins:
        return -1

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in usable_coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] <= total else -1
