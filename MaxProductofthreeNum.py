def maxProduct(n:list[int])->int:
    max1=max2=max3=float('-inf')
    min1=min2=float('inf')
    for num in n:
        
        if num>max1:
            max3=max2
            max2=max1
            max1=num
        elif num>max2:
            max3=max2
            max2=num
        elif num>max3:
            max3=num
    m1=max1*max2*max3
    for num in n:
        
        if num<min1:
            min2=min1
            min1=num
        elif num<min2:
            min2=num    
    m2=min1*min2*max1

    return max(m1,m2)

def main():
    nums=list(map(int,input(f"enter numbers seperated by space: ").split()))
    print(f"Maximum producct of three Number: {maxProduct(nums)}")

if __name__=="__main__":
    main()    