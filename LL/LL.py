class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        #verifying if the linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
        #if the linked list is not empty
        else:

            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
    
    def pop(self):

        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        #decrementing the length
        self.length -= 1
        #if the length is 0, the head and tail should be None crack the problem
        if self.length == 0:
            self.head = None
            self.tail = None
            return None
        #returning the popped node
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        #if the linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        # incrementing the length
        self.length += 1
        return True
    
    def pop_first(self):
        
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp

    def get(self, index):
        if index < 0 or index>= self.length:
            return None
        temp =self.head
        for _ in range(index):
            temp = temp.next
        return temp
    

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        else:
            return False
        
    def insert(self, index, value):

        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)        
        
        new_node = Node(value)
        temp = self.get(index-1)
        #saving the next of the previous node
        new_node.next = temp.next
        #updating the next of the previous node
        temp.next = new_node
        
        #incrementing the length
        self.length += 1

        return True


    def remove(self, index):

        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        #getting the previous node
        prev = self.get(index - 1)
        temp = prev.next
        #updating the next of the previous node
        prev.next = temp.next
        #updating the next of the removed node
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head
        temp = self.head
        self.head = self.tail
        self.tail = temp
    
        #iterating through the linked list
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        

my_linkdlist = LinkedList(1)
my_linkdlist.append(2)
my_linkdlist.append(3)
my_linkdlist.append(4)

my_linkdlist.reverse()

# print(my_linkdlist.remove(2), '\n')
my_linkdlist.print_list()

#passing the index(position) of the node to be printed
#print(my_linkdlist.get(2))

