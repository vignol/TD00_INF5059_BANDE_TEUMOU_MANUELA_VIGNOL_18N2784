def max_subarray_sum(numbers):
    if len(numbers) == 0:
        return 0
    max_sum = numbers[0] 
    current_sum = numbers[0] 
    for i in range(1, len(numbers)):
        current_sum = max(numbers[i], current_sum + numbers[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
print(max_subarray_sum([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]))  
print(max_subarray_sum([9,10,14,-4,3,-1,9]))

