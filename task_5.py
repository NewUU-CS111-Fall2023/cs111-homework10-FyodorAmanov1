def find_triplet_with_sum_zero(nums):
    n = len(nums)

    # Sort the array to simplify the search for triplets
    nums.sort()

    for i in range(n - 2):
        # Fix the first element of the triplet
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # Triplet found
                return [nums[i], nums[left], nums[right]]
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    # No distinct triplet with sum zero found
    return None

# Example usage:
numbers = list(map(int, input().split()))
result = find_triplet_with_sum_zero(numbers)

if result:
    print("Triplet with sum zero:", result)
else:
    print("No distinct triplet with sum zero found.")
