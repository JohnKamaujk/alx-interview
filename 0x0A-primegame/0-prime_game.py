#!/usr/bin/python3
"""Prime game module.
"""


def generate_primes(max_num):
    """
    Generate a list of prime numbers up to a given maximum number.
    Args:
        max_num up to which prime numbers will be generated.
    Returns:
        list: A list of boolean values indicating whether each number is prime.
              True for prime, False for non-prime.
    """
    primes = [True] * max_num
    primes[0] = False
    for i in range(2, max_num + 1):
        if primes[i - 1]:
            for j in range(i * 2, max_num + 1, i):
                primes[j - 1] = False
    return primes


def count_wins(primes, rounds):
    """
    Count the wins for Maria and Ben based on the given primes and rounds.
    Args:
        primes (list): A list of boolean values indicating whether each number
                         is prime.True for prime, False for non-prime.
        rounds (list): A list of integers representing the maximum
                        number for each round.
    Returns:
        tuple: A tuple containing the counts of wins for Maria and Ben.
    """
    marias_wins, bens_wins = 0, 0
    for round_num in rounds:
        primes_count = sum(primes[:round_num])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    return marias_wins, bens_wins


def isWinner(x, nums):
    """
    Determine the winner of a prime game with `x` rounds.
    Args:
        x (int): The number of rounds in the game.
        nums (list): A list representing the max number for each round.
    Returns:
        str or None: The name of the player who won the most rounds,
                     or None if the winner cannot be determined.
    """
    if x < 1 or not nums:
        return None
    max_num = max(nums)
    primes = generate_primes(max_num)
    marias_wins, bens_wins = count_wins(primes, nums)
    if marias_wins > bens_wins:
        return 'Maria'
    elif marias_wins < bens_wins:
        return 'Ben'
    else:
        return None
