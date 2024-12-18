class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
currentnode=head
for i in range(2,10):
    newnode=Node(i)
    currentnode.next=newnode#here we are used to link the next node to the current node.
    currentnode=newnode#here we are used to update the current node 
print(currentnode.data)# here it traverse from 2 to 9 at last the value will be 9.
currentnode=head# we are reinitialized it to head
newnode1=Node(45)
#Here i want to insert the element at the middle and after the 6 i want to insert
temp=head
while temp.next!=None:
    if temp.data==5:
        break
    temp=temp.next
if temp!=None:
    newnode1.next=temp.next
    temp.next=newnode1
currentnode=head
while currentnode is not None:# so it is used to traverse each node
    print(currentnode.data,end="")
    if currentnode.next is not None:
        print("->",end="")
    currentnode=currentnode.next
