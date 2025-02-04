def search_binary(sorted_list, target):
    left=0
    right = len(sorted_list) - 1
    
    while left<=right:
        middle=(left+right)//2
        if sorted_list[middle]==target:
            return middle
        elif sorted_list[middle]<target:
            left=middle+1
        else:
            right=middle-1
    return -1
sorted_list = [4,9,17,-3,107,-2,9]
print(search_binary(sorted_list, 9)) 
print(search_binary(sorted_list, -3)) 
print(search_binary(sorted_list, 3)) 
