#!/usr/bin/python3
""" Making change."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Parameters:
    coins (list): A list of integers representing the values of the coins
    in your possession.
    total (int): The total amount you want to achieve with the fewest number
    of coins.

    Returns:
    int: The fewest number of coins needed to meet the total. 
         If the total is 0 or less, returns 0.
         If the total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize dp array with a large number (inf)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Iterate through each amount from 1 to total
    for t in range(1, total + 1):
        # Check each coin denomination
        for coin in coins:
            if coin <= t:
                # Update the dp array with the minimum number of coins needed
                dp[t] = min(dp[t], dp[t - coin] + 1)

    # If dp[total] is still inf, it means the total cannot be met with
    return dp[total] if dp[total] != float('inf') else -1
