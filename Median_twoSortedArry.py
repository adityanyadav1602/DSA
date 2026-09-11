def Merge(list1 ,list2):
    if not list1: return list2
    if not list2: return list1
    list=[]
    #if len(list1)==1 and len(list2)==1:
        #return [list2[0],list1[0]] if list1[0]>list2[0] else [list1[0],list2[0]]
        #it cover in bellow while loop
    i,j=0,0
    while i < len(list1) and j < len(list2):
        if list1[i]>list2[j]:
            list.append(list2[j])
            j+=1
        else:
            list.append(list1[i])  
            i+=1
    if i<len(list1):
        list.extend(list1[i:])
    if j<len(list2):
        list.extend(list2[j:])

    return list
def Median(list)->float:
    n=len(list)
    if n==0: return None

    if n%2==0:
        return float((list[n//2-1]+list[n//2])/2)#// (Double Slash) = Integer Division (Floor Division),
        #/(single slash)Float Division ke liye hota hai
    else:
        return float(list[n//2])

def main():
    list1=[1]
    list2=[1]

    list=Merge(list1,list2)
    print("Merge Array: ",list)
    median=Median(list)
    print("Median= ",median)

if __name__=="__main__":
    main()     