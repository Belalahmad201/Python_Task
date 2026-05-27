def move_zeroes(nums):
    j = 0   # position for next non-zero element

    # Move non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    return nums


# Example
nums = [0, 1, 0, 3, 12]
print("Output:", move_zeroes(nums))