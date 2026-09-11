class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

    def display_LL(self):
        head=self

        print("...LinkList...: ")

        while head is not None:
            print(head.data, end="--->")
            head=head.next

        print("None")           

def main():

    print("Enter data in node :",end="\n")
    data1=int (input("First node: "))
    data1=Node(data1)
    data2=int(input("Second node: "))
    data2=Node(data2)
    data1.next=data2
    data3=int(input("third node: "))
    data3=Node(data3) 
    data2.next=data3
    data4=int(input("fourth node: "))
    data4=Node(data4) 
    data3.next=data4
    data5=int(input("fifth node: "))
    data5=Node(data5)
    data4.next=data5

    data1.display_LL()

if __name__=="__main__":
    main()    
    

