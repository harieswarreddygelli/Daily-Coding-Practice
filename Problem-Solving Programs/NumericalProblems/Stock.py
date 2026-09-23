def maxProfit(prices):
    minSoFar = prices[0]
    res = 0 
    for i in range(1, len(prices)):  
        minSoFar = min(minSoFar, prices[i])              
        res = max(res, prices[i] - minSoFar) 
    return res
prices=list(map(int,input("Enter the prices of this week: ").split()))
print("The Maximum profit of this week is:",maxProfit(prices))
