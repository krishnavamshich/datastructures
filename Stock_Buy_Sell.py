def maxProfit(arr, N):
    i = 0;
    while(i<N):
        #Go till you find a minimum price to buy
        while(i<N-1 and arr[i]>arr[i+1]):
            i+=1;
        print("Buy :"+str(i), end="  ");
        #Go till you find maximum to sell
        while(i<N-1 and arr[i]<arr[i+1]):
            i+=1;
        print("Sell :"+str(i));
        i+=1;

arr = [100, 180, 260, 310, 40, 535, 695];
maxProfit(arr, len(arr));
