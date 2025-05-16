class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
   def __init__(self, value):
      self.value = value
      self.next = None

    
    #################################
        
class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    def __init__(self, value):
       new_node = Node(value)
       self.head = new_node
       self.tail = new_node
       self.length = 1
    ###############################
    #PRINTING A LINKED LIST
    def print_list(self):
       temp = self.head
       while temp is not None:
          print(temp.value)
          temp = temp.next

    ##APPEND AT THE END OF THE LINKEDLIST
    def append(self, value):
            new_node = Node(value)

            if self.length == 0:
                self.head = new_node
                self_tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length+=1
            return True
    
    def pop(self):
        
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        
        while(temp.next):
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp
    
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
       
       if self.length == 0:
           return None
       
       temp = self.head
       self.head = self.head.next
       temp.next = None
       self.length -= 1

       if self.length == 0:
           self.tail = None
       return temp
    
    def get(self, index):

        if index < 0 or index > self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


 
my_linked_list = LinkedList(2)

my_linked_list.append(3)

my_linked_list.prepend(1)

my_linked_list.print_list()

# # (2) Items - Returns 2 Node
# print(my_linked_list.pop().value)
# # (1) Item -  Returns 1 Node
# print(my_linked_list.pop().value)
# # (0) Items - Returns None
# print(my_linked_list.pop())
                          
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    