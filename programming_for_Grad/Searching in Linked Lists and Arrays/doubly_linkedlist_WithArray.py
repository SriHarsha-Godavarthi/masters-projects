import random
import time

from customFunctions import binaryInsertion
# class Node is used for creating node for attaching to linked list
class Node:
    def __init__(self,valueOfNode=None):
        #create a node in linkedList
        #In doubly linked list each node will have three properties one is previous,next,data 
        self.previous=None
        self.data=valueOfNode
        self.next=None
# class linkedList is used for creating,appending,deleting,traverse the linked list
class SingleLinkedList:
    def __init__(self):
        #create empty linked list
        self.head=None
        
    def appendNode(self,data):
        if self.head is None:
            #if head is Node then attach first (or) create Node 
            self.head=Node(data)
        else:
            # attach newly created nodes  if the linked list have one (or) more nodes
            # point head to newly created Node
            # store the previous head node and point it's previous pointer to newnode 
            #  newnode next pointer to previous head node
            current=self.head
            self.head = Node(data)
            current.previous=self.head
            self.head.next = current
        return self.head
    
    def insertNode(self,data,isAscendingOrder):
        newElement=Node(data)
        current=self.head
        previousPointer=self.head
        #loop until all elements in linked list are traversed
        while current:
           if  isAscendingOrder:
               if current.data>=newElement.data:
                   break
               else:
                   #if condition not satisfied the check for next element
                    previousPointer=current
                    current=current.next
                  
           else:
                if current.data<=newElement.data:
                   break
                else:
                        #if condition not satisfied the check for next element value
                        previousPointer=current
                        current=current.next
        # inserting the element without disturbing sorting order
        if current is None:
            #insert in Last Place
                previousPointer.next=newElement
                newElement.previous=previousPointer
        elif (current.previous is not None ):
            #insert in middle of linked list
                previous=current.previous
                previous.next=current.previous=newElement
                newElement.next=current
        elif (current.previous is None):
            #insert in starting of linked list
                self.head=newElement
                newElement.next=current
                current.previous=newElement
        return self.head
        
    def traverse(self):
        linkedListStr=""
        if self.head is None:
            #if linked list is doesn't have any nodes
            print("empty linkedList")
        elif self.head.next is None:
            #if linked list have single node
            print("elements in linked List are:\n",self.head.data)
        else:
            #if linked list have more than one node
            current=self.head
            print("elements in linked List are:\n")
            while current.next is not None:
                linkedListStr+=str(current.data)+"->"
                current=current.next
            linkedListStr+=str(current.data)
            print(linkedListStr)
            
    # def findMiddleAddress(self,head):
    #     # intialize slow and fast with head
    #     #increase fast by 2 steps and slow by one
    #     #so we will get middle element in linked list by accessing slow pointer
    #     slow=fast=head
    #     while True:
    #         if fast.next is None:
    #             break
    #         elif fast.next.next is None:
    #             break
    #         fast=fast.next.next
    #         slow=slow.next
    #     #split the linked list and return head pointer for second half
    #     middlePosition=slow.next
    #     slow.next=None
    #     middlePosition.previous=None
    #     return middlePosition
    
    # def mergeSort(self, head,isAscendingOrder):
    #     # this function is used for sort linked list
    #     # if head is None or have single Node No need to sort Just Return
    #     if head is None:
    #         return head
    #     if head.next is None:
    #         return head
    #     # find the middleAddress after dividing the linked list
    #     second = self.findMiddleAddress(head)
    #     # Recurrsivly sort for left and right halves
    #     # perform mergeSort on left half 
    #     head = self.mergeSort(head,isAscendingOrder)
    #     # perform mergeSort on second half 
    #     second = self.mergeSort(second,isAscendingOrder)
    #     # merge the two half's after sorting
    #     return self.merge(head,second,isAscendingOrder)
    
    # def merge(self,firstHead,secondHead,isAscendingOrder):
    #     if firstHead is None:
    #         return secondHead
    #     if secondHead is None:
    #         return firstHead
    #     if isAscendingOrder:
    #         if firstHead.data < secondHead.data:
    #     # In ascending order  by the above mentioned condition firstHead->data lessthan secondHead->data
    #     # so point firstNext.next to secondHead 
    #     # also point secondHead.previous (i.e firstHead.next.previous to firstHead)
    #     # remove the previous pointer for firstHead
    #     # return the merged linked list
    #             firstHead.next = self.merge(firstHead.next, secondHead,isAscendingOrder)
    #             firstHead.next.previous = firstHead
    #             firstHead.previous = None  
    #             return firstHead
    #         else:
    #     # opposite of above mentioned one
    #             secondHead.next = self.merge(firstHead, secondHead.next,isAscendingOrder)
    #             secondHead.next.previous = secondHead
    #             secondHead.previous = None
    #             return secondHead
    #     else:
    #         if firstHead.data<secondHead.data:
    #     # In descending order  by the above mentioned condition firstHead->data lessthan secondHead->data
    #     # so point secondHead.next to firstHead 
    #     # also point secondHead.previous (i.e secondHead.next.previous to secondHead)
    #     # remove the previous pointer for secondHead
    #     # return the merged linked list
    #             secondHead.next = self.merge(firstHead, secondHead.next,isAscendingOrder)
    #             secondHead.next.previous=secondHead
    #             secondHead.previous=None
    #             return secondHead
    #         else:
    #     # opposite of above mentioned one
    #             firstHead.next = self.merge(firstHead.next, secondHead,isAscendingOrder)
    #             firstHead.next.previous=firstHead
    #             firstHead.previous=None
    #             return firstHead

    def deleteAt(self,position,lengthOfLinkedList):
        current = self.head
        count=0
        if self.head is None:
            print("empty linkedList")
        elif self.head.next is None:
            if position==count:
                self.head=None
            else:
                print("element not found")
        else:
            current=self.head
            while count!=position and count<=lengthOfLinkedList:
                if current.next is not None:
                    current=current.next
                    count+=1
                elif current.next is None:
                    if count==position:
                        current=current.previous
                        current.next = None
            if count==position:
                if (current.next is not None) and (current.previous is not None):
                    #if deleting element is not at start or end element
                    previous=current.previous
                    previous.next=current.next
                    current=current.next
                    current.previous=previous
                elif (current.previous is None):
                    #if deleting element is firt element
                    self.head=current.next
                elif (current.next is None):
                    #if deleting element is last element
                    current.previous.next=None
            else:
                print("no element found")
                     
        return self.head
    
    # def deleteNode(self,elementToDelete):
    #     current = self.head
    #     if self.head is None:
    #         print("empty linkedList")
    #     elif self.head.next is None:
    #         if self.head.data==elementToDelete:
    #             self.head = None
    #         else:
    #             print("element not found")
    #     else:
    #         current=self.head
    #         while current.data != elementToDelete:
    #             if current.next is not None:
    #                 current=current.next
    #             elif current.next is None:
    #                 if current.data == elementToDelete:
    #                     current=current.previous
    #                     current.next = None
    #         if current.data == elementToDelete:
    #             if (current.next is not None) and (current.previous is not None):
    #                 #if deleting element is not at start or end element
    #                 previous=current.previous
    #                 previous.next=current.next
    #                 current=current.next
    #                 current.previous=previous
    #             elif (current.previous is None):
    #                 #if deleting element is firt element
    #                 self.head=current.next
    #             elif (current.next is None):
    #                 #if deleting element is last element
    #                 current.previous.next=None
                     
    #     return self.head
    
    def convertToArray(self):
        random_list=[]
        if self.head is None:
            return random_list
        elif self.head.next is None:
            random_list.append(self.head.data)
            return random_list
        else:
            current=self.head
            # print("elements in linked List are:\n")
            while current.next is not None:
                random_list.append(current.data)
                current=current.next
            random_list.append(current.data)
            return random_list
    
    def convertArrayToLinkedList(self,randomList):
        self.head = None
        if len(randomList)==0:
            self.head = None
        else:
            randomList.reverse()
            for element in randomList:
                self.appendNode(element)
        return self.head
                
                
       
#get the values for both upperbound(maximum_range) and number of random elements to be generated
maximum_range=int(input("enter maximum range for an element\n"))
number_of_elements=int(input("enter number of elements\n")) 
# maximum_range=100
# number_of_elements= 12
#create linked list
# Get the current time before executing the code
starttime = time.time_ns()  
linkedList= SingleLinkedList()
isAscendingOrder = False
greaterThanFifty = 0
initialValue=1
while initialValue<=number_of_elements:
    random_number=random.randint(1,maximum_range)
    if greaterThanFifty<=5 and random_number>50:
        greaterThanFifty+=1
        if greaterThanFifty>5:
            isAscendingOrder=True
    if initialValue==1:
        linkedList.head=linkedList.appendNode(random_number)
    else:
        linkedList.appendNode(random_number)
    initialValue+=1
    
linkedList.traverse()
# linkedList.head=linkedList.mergeSort(linkedList.head,isAscendingOrder)
# linkedList.traverse()
# if isAscendingOrder and number_of_elements>=5:
#     linkedList.head=linkedList.deleteAt(4,number_of_elements-1)
#     linkedList.traverse()
# elif ((not isAscendingOrder) and number_of_elements>2):
#     linkedList.head=linkedList.deleteAt(1,number_of_elements-1)
#     linkedList.traverse()
    
# linkedList.insertNode(10,isAscendingOrder)
# linkedList.traverse()
randomList= linkedList.convertToArray()
print("Converted to array",randomList)

# for element in randomList:
#     if greaterThanFifty<=5 and element>50:
#         greaterThanFifty+=1
#     if greaterThanFifty>5:
#         #sort elements in increasing order and delete 5th element
#         randomList.sort()
#         if(number_of_elements>=5):
#          randomList.pop(4)
#         isAscendingOrder = False
#         break
if greaterThanFifty<=5:
    #sort elements in descending order and delete 2nd element
    randomList.sort(reverse=True)
    if(number_of_elements>=2):
     randomList.pop(1)
else: 
        randomList.sort()
        if(number_of_elements>=5):
         randomList.pop(4)

position=binaryInsertion(randomList,10,isAscendingOrder)
randomList.insert(position,10)
linkedList.head=linkedList.convertArrayToLinkedList(randomList)
linkedList.traverse()
# getting the time taken for executing the code
endtime = time.time_ns()

# Printing the time taken for code execution
executionTime = endtime - starttime
print('CPU Execution time:', executionTime)
# linkedList.traverse()
# deleteElement=int(input("Enter Vaue To Delete:"))
# linkedList.head=linkedList.deleteNode(deleteElement)
# linkedList.traverse()

# print(f"The below mentioned is the final sorted list \n {randomList}\n position to insert \n{position}")