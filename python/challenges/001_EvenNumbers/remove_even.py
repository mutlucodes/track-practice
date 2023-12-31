def remove_even_numbers(nums):
    odd_numbers = []
    for i in nums:
        if i%2 != 0:
            odd_numbers.append(i)

    
    return odd_numbers