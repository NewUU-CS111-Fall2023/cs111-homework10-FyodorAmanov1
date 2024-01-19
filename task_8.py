def can_partition(nums):
    total_sum = sum(nums)

    # If the total sum is odd, it's not possible to partition into two subsets with equal sums
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    n = len(nums)

    # Create a 2D array to store whether a subset with a given sum is possible
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Initialization: A subset with sum 0 is always possible
    for i in range(n + 1):
        dp[i][0] = True

    # Dynamic programming to fill the table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

    return dp[n][target_sum]
