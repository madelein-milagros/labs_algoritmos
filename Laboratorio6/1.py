#1
from collections import deque

def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []

    result = []
    dq = deque()  # Store indices of elements

    for i in range(len(nums)):
        # Remove indices that are out of this window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements smaller than current from the deque
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add current element index
        dq.append(i)

        # Append max value to result when we have the first full window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))  # Output: [3, 3, 5, 5, 6, 7]

