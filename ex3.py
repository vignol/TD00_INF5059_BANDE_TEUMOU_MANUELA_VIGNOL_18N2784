def knapsack(elements, W):
    dp=[0]*(W+1)
    for value, weight in elements:
        for w in range (W, weight-1, -1):
            dp[w]=max(dp[w-weight]+value, dp[w])
    max_val=dp[W]
    choosen_elmts=[]
    w=W
    for x in range(len(elements)-1,-1,-1):
        value, weight=elements[x]
        if dp[W]==dp[w-weight]+value and w>=weight:
            choosen_elmts.append(elements[x])
            w = w - weight 
    choosen_elmts.reverse()
    return choosen_elmts, max_val

elmts=[(5,70),(10,120),(7,70),(5,80),(13,100)]
choosen_elmts, max_val=knapsack(elmts,200)
print("Selected elements:")
for element in choosen_elmts:
    print(f"Value: {element[0]}, Weight: {element[1]}")
print(f"Maximum value: {max_val}")