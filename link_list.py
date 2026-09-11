class Node:
    def __init__(self, data):  #blueprint of node
        self.data=data
        self.next=None


class Linklist:
    def __init__(self):
        self.head=None #initialization  

    def create_LL(self,data):
        
        new_node=Node(data)
        #first node ko header bana do aur return ho jao..
        if self.head is None:
            self.head=new_node
            return 
        #ye last var keval move karane ke lye hai mai ise head ke jagah replace kar raha hu:
        last=self.head

       #check jab tak yah none n ho jaye:paheli bar aya to last.next==None tha so vah loop ke andar nahi jayega

        while last.next:
            last=last.next    #last.next!= None then move last to next node

        #if last.next==None so naya node uske piche jud jayega  

        last.next=new_node       

    def display(self):
        current=self.head  #header node assine karenge n kikeval srlf koi ki self ne next nahi hai

        print(".....LL....:",end="\n")

        while current.next is not None:
            print(current.data,end="-->")
            current=current.next

        print("None")    

        


def main():
    ll=Linklist()

    ll.create_LL(20)
    ll.create_LL(38)
    ll.create_LL(50)
    ll.create_LL(43)
    ll.create_LL(45)

    ll.display()

if __name__=="__main__":
    main()