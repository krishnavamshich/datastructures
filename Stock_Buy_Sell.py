def maxProfit(arr, N):
    i = 0;
    sol = [];
    while(i<N-1):
        #Go till you find a minimum price to buy
        while(i<N-1 and arr[i]>arr[i+1]):
            i+=1;
        if(i==N-1):
            break;
        
        x=i;
        #Go till you find maximum to sell
        while(i<N-1 and arr[i]<=arr[i+1]):
            i+=1;
        y=i;
        sol.append((x,y));
    return sol;


arr = [100, 180, 260, 310, 40, 535, 695];
ans = maxProfit(arr, len(arr));

for el in ans:
    print("("+str(el[0])+" "+str(el[1])+")", end=" ");
if(len(ans)==0):
    print("No Profit", end="");
print()
