#!/usr/bin/python3
"""
Making change module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values,
    using a greedy approach.
    Args:
        coins (list of int): The denominations of coins available.
        total (int): The total amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total amount.
            Returns -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order

    coins_count = 0
    idx = 0

    while total > 0 and idx < len(coins):
        if coins[idx] <= total:
            total -= coins[idx]
            coins_count += 1
        else:
            idx += 1

    if total == 0:
        return coins_count
    else:
        return -1
