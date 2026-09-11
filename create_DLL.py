class DNode:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class Dubble_LL:
    def __init__(self):
        self.head=None
        self.tail=None

    def Creat_DLL(self,new_node):
        new_node=DNode(new_node)

        if self.head is None:
            self.head=new_node
            return

        temp=self.head

        while temp.next:
            temp=temp.next

        temp.next=new_node 
        new_node.prev=temp
        self.tail=new_node



    def display(self):
        if self.head is None:
            print("...Empty_DLL...")
            return

        current=self.head
        print("....DLL in Forword direction...",end="\n")

        while current is not None:

            print(current.data, end="<--->")  
            current=current.next
        
        print("None")   

        print("....DLL in backtracking...",end="\n")

       
        last=self.tail
        while last:
            print(last.data,end="<--->")
            last=last.prev
        print("None")    

       
 
def main():
    ll=Dubble_LL()
    ll.Creat_DLL(10)
    ll.Creat_DLL(20)
    ll.Creat_DLL(30)
    ll.Creat_DLL(40)

    ll.display()
if __name__=="__main__":
    main()    


