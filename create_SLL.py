class SNode:
    def __init__(self, data):
        self.data=data
        self.next=None

    def Create_node(self,  list):
       # head=list[0]
        for i in range(len(list)-1):
            list[i].next=list[i+1]

        #return head 
        return list[0]   
            
    def display(self):
        #head=self
        current=self
        print("....LINK_LIST......",end="\n")

        while current is not None:
            print(current.data,end="-->")
            current=current.next

        print("None")    

        

def main():
    data1=int (input("First node: "))
    data1=SNode(data1)
    
    data2=int(input("Second node: "))
    data2=SNode(data2)
        
    data3=int(input("third node: "))
    data3=SNode(data3) 
        
    data4=int(input("fourth node: "))
    data4=SNode(data4) 
        
    data5=int(input("fifth node: "))
    data5=SNode(data5)

    ll_list=[data1,data2,data3,data4,data5]

    head=data1.Create_node(ll_list)

    head.display()

if __name__=="__main__":
    main()    
      
                