class Node:      #Node class 
    def _init_(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:       #SLL class to create singly linked list
    def _init_(self, start=None):
        self.start = start
    
    def is_empty(self):
        self.start == None
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_end(self, data):
        n = Node(data) #value of next is none automatically
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next

        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
        
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()


    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None


    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def _len_(self):
        temp = self.start
        count = 0
        while temp is not None:
            temp = temp.next
        count +=1

    def _iter_(self):
        return SLLIterator(self.start)
    

                 
class SLLIterator:
    def _init_(self, start):
        self.current = start

    def _iter_(self):
        return self
    
    def _next_(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
    





         

#driver_code
my_list = SLL()

my_list.insert_at_start(10)
my_list.insert_at_start(20)
my_list.insert_at_start(30)
my_list.insert_after(my_list.search(30), 40)
my_list.insert_after(my_list.start.next.next, 50)
my_list.insert_after(my_list.search(40), 60)
my_list.delete_item(60)
my_list.print_list()
for x in my_list:
    print(x, end=" ")
print()

print(my_list.start.next.next.item)