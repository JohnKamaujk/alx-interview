#!/usr/bin/python3
"""Making change module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    # list to store the fewest coins needed to make each amount from 0 to total
    min_coins_needed = [float('inf')] * (total + 1)
    min_coins_needed[0] = 0  # Base case: 0 coins needed to make amount 0

    for coin in coins:
        # Update min_coins_needed[i] if using this coin reduces the number
        # of coins needed to make amount i
        for i in range(coin, total + 1):
            min_coins_needed[i] = min(min_coins_needed[i],
                                      min_coins_needed[i - coin] + 1)

    # If min_coins_needed[total] is still float('inf'), total
    # cannot be met by any combination of coins
    if min_coins_needed[total] != float('inf'):
        return min_coins_needed[total]
    else:
        return -1
