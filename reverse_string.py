def rev_strbuiltin(s: str)->str:
    return s[::-1]

def rev_strmanual(s: str)->str:
    s_list=list(s)
    l=0
    r=len(s_list)-1
    while l<r:
        s_list[l],s_list[r]=s_list[r],s_list[l]
        l+=1
        r-=1

    return ''.join(s_list)
#''.join()-->yah list ke char ko chipka deta hai aur ise string bana deta hai:like: ','.join(list):o/p:a,b,c if list=['a','b','c']
def main():
    s=input("enter string: ")
    print(f"rev_string: {rev_strbuiltin(s)}")
    s=input("Enter string: ")
    print(f"rev_string: {rev_strmanual(s)}")  

if __name__=="__main__":
    main()          