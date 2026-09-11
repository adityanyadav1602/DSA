def rev_num(n:int)->int:

    rev_str=str(abs(n))[::-1]
    r_num=int(rev_str)

    if r_num > (2**31 -1):
        return 0
    
    return r_num if n>=0 else -r_num

def main():
    x=int(input("Number= "))
    print(f"Reverse Number: {rev_num(x)}")

if __name__=="__main__":
    main()        