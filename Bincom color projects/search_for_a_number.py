def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Not found

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
numbers = [1, 2, 4, 7, 10, 14, 17, 19, 23]
target_number = int(input("Enter the number to search for: "))

result = binary_search_recursive(numbers, target_number, 0, len(numbers) - 1)

if result != -1:
    print(f"The number {target_number} was found at index {result}.")
else:
    print(f"The number {target_number} was not found.")