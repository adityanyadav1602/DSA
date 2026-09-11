def threeSum(nums: list[int])->list[list[int]]:#a=[-1,0,1,2,-1,-4]
    list=[]
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        j=i+1
        k=len(nums)-1

        while j<k:
            total=nums[i]+nums[j]+nums[k]

            if total==0:
                list.append([nums[i],nums[j],nums[k]])
                
                #avoid dublicating
                while j<k and nums[j]==nums[j+1]:
                    j+=1

                while k>j and nums[k]==nums[k-1]:
                    k-=1
                #if elements are not same
                j+=1
                k-+1

            elif total<0:
                j+=1
            else :
                k-=1

    return list                    

def main():
    a=[-1,0,1,2,-1,-4]
    print(f"3Sum triplat list : {threeSum(a)}")

if __name__=="__main__":
    main()    


    

