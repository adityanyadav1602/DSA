def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        extra_node=ListNode(0)
        current=extra_node
        carry=0

        while l1 is not None or l2 is not None or carry!=0:

           if l1 is not None:
             t1=l1.val
           else:
              t1=0
           if l2 is not None:
              t2=l2.val 
           else:
              t2=0 

           total = t1 + t2 + carry
           rem = total%10
           carry = total//10

           current.next = ListNode(rem)
           current = current.next
            
           if l1: l1=l1.next
           if l2: l2=l2.next    

        return extra_node.next
