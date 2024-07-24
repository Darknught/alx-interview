#!/usr/bin/python3
""" Making change."""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Parameters:
    coins (list): A list of integers representing the denominations
    of the coins.
    total (int): The total amount to be formed using the fewest number
    of coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
         Returns 0 if the total is 0 or less.
         Returns -1 if the total cannot be met by any number of coins.
    """

    # If total is 0 or negative, no coins are needed
    if total <= 0:
        return 0

    # Initialize the dp array with infinity, as we are looking for the minimum
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Iterate over each amount from 1 to total
    for t in range(1, total + 1):
        # Check each coin denomination
        for coin in coins:
            if coin <= t:
                # If coin can be used, update dp[t] to the minimum coins needed
                dp[t] = min(dp[t], dp[t - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be formed
    return dp[total] if dp[total] != float('inf') else -1
