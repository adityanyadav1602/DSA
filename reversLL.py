def revLL(self,head):
            t1=None 
            t2=None
            current=self.head
            while current is not None:
                t2=current.next
                currrent.next=t1
                t1=current
                current=t2
            self.head=t1
            return self.head 