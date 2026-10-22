# src/divide_conquer.py

def find_max_crossing_subarray(arr, low, mid, high):
    """Finds the maximum subarray crossing the midpoint."""
    left_sum = float('-inf')
    current_sum = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i

    right_sum = float('-inf')
    current_sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        current_sum += arr[j]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def max_subarray_divide_conquer(arr, low, high):
    """Recursive Divide-and-Conquer maximum subarray algorithm."""
    if low == high:
        return low, high, arr[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = max_subarray_divide_conquer(arr, low, mid)
    right_low, right_high, right_sum = max_subarray_divide_conquer(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum