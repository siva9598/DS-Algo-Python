class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        if(self.head ==None):
            self.head = new_node
            return
        else:
            last =self.head
            while(last.next):
                last= last.next
            last.next =new_node

    def remove(self,data_to_remove):
        #new_node = Node(new_data)
        if(self.head.next == None):
            self.head == None
            return
        else:
            current = self.head
            while(current.next):
                if(current.next.data == data_to_remove):
                    temp = current.next
                    current.next= temp.next
                    return
                else:
                    current = current.next
    def getLength(self):
        if(self.head == None):
            return 0
        else:
            current = self.head
            length =1
            while(current.next):
                length =length +1
                current =current.next
            return length



    def show(self):
        temp =self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def nthElement(self,n):
        if (self.head == None):
            return "nth element not found"
        current =self.head
        l=1
        while(current.next):
            if(l==n):
                return current.data
            else:
                current = current.next
                l= l+1
        if(l<n):
            return "list length is less than n elements"

    def middleElement_double_pointer(self):
        if (self.head == None):
            return 0
        elif(self.head.next == None):
            return self.head
        else :
            fast = self.head
            slow = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow.data

    def detectLoop(self):
        fast = self.head
        slow = self.head
        hasLoop = False
        while( slow and fast and fast.next):
                slow = slow.next
                fast = fast.next.next
                if(fast == slow):
                    hasLoop = True
        return hasLoop

    def checkPalindrone(self):
        reversal_stack = []
        current = self.head
        while (current):
            reversal_stack.append(current.data)
            current = current.next
        check_ptr = self.head
        while (check_ptr):
            if (check_ptr.data == reversal_stack[-1]):
                reversal_stack.pop()
            check_ptr = check_ptr.next
        if (len(reversal_stack) == 0):
            return True
        else:
            return False

    def swapNodes(self, x, y):
        # get the previous value of x and previous value of y, then change the previous X's next to
        # point to current Y.Then change the next of current X to previous Y.
        if x == y:
            return

        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX == None or currY == None:
            return
        if prevX != None:
            prevX.next = currY
        else:  # make y the new head
            self.head = currY

        if prevY != None:
            prevY.next = currX
        else:  # make x the new head
            self.head = currX

        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def pairWiseSwapData(self):
        current =self.head
        if current is None:
            return
        while(current and current.next):
            if(current.data != current.next.data):
                current.data, current.next.data = current.next.data,current.data

            current= current.next.next

    def oddEvenSegregate(self):

        oddList = LinkedList()
        evenList = LinkedList()
        current = self.head

        while (current):
            if (current.data % 2 == 0):
                evenList.push(current.data)
            else:
                oddList.push(current.data)
            current = current.next
        odd_ptr = oddList.head
        while (odd_ptr):
            evenList.push((odd_ptr.data))
            odd_ptr = odd_ptr.next
        evenList.show()

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printrev(self, temp):

        if temp:
            self.printrev(temp.next)
            print(temp.data, end=' ')
        else:
            return

###### multi linked list functions

def intersection(a, b):
    c = LinkedList()
    current_a =a.head
    current_b =b.head
    while (current_a != None and current_b != None):
        if (current_a.data == current_b.data):
            c.push(current_a.data)
            current_a = current_a.next
            current_b = current_b.next
        elif (current_a.data < current_b.data):
            current_a = current_a.next
        else:
            current_b = current_b.next

    return c
def intersectionPoint(a,b):
    a_ptr =a.head
    b_ptr =b.head
    a_length =0
    b_length =0
    while(a_ptr):
        a_length =a_length +1
        a_ptr =a_ptr.next
    while (b_ptr):
        b_length = b_length + 1
        b_ptr = b_ptr.next
    diff_length = abs(a_length-b_length)

    a_ptr = a.head
    b_ptr = b.head
    if(a_length>b_length):
        while(diff_length!=0):
            curr = a_ptr
            a_ptr = a_ptr.next
            diff_length= diff_length-1
        return curr.data
    elif (a_length < b_length):
        while (diff_length != 0):
            curr = b_ptr
            b_ptr = b_ptr.next
            diff_length = diff_length - 1
        return curr.data





llist = LinkedList()
llist.push(7)
llist.push(8)
llist.push(9)
llist.push(10)

llist.show()
llist.remove(3)
llist.show()
print(llist.getLength())
print(llist.nthElement(2))
