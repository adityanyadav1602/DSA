def get_reverse(n: int)->int:
    sign=-1 if n<0 else 1

    x=0
    n=abs(n)#b/c, (a // b) * b + (a % b) == a, 123%10=3 but -123%10=7 which is incurrect 

    while n>0:
            rem=n%10
            x=x*10+rem
            n//=10

    return sign*x   
def main():
    x=int(input("enter num: "))
    print(f"Reverse num: {get_reverse(x)}")

if __name__=="__main__":
    main()                      