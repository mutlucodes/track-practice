# Remove Even Numbers Function
def remove_even_numbers(nums):
    """
    Remove all even numbers from a list and return a new list containing only the odd numbers.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A list containing only the odd numbers from the original list.
    """
    odd_numbers = []
    for i in nums:
        if i%2 != 0:
            odd_numbers.append(i)
    return odd_numbers
