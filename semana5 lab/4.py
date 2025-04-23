from collections import deque

def sliding_window_max(nums, k):
    if not nums or k <= 0:
        return []

    result = []
    dq = deque()  # Store indices, not values

    for i in range(len(nums)):
        # Remove indices that are out of the window range
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices whose values are less than the current value
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add the current index to the deque
        dq.append(i)

        # Add the maximum of the current window to the result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Test
if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("Sliding window maximums:", sliding_window_max(nums, k))
    # Expected output: [3, 3, 5, 5, 6, 7]
