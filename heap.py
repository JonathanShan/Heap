
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.capacity = capacity
        self.size = 0
        self.heap = [None] * (self.capacity+1)

    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased"""
        if self.capacity < len(alist):
            self.heap = self.heap + [None]*(len(alist) - self.capacity)
            self.capacity = len(alist)
        for i in range(len(alist)):
            self.heap[i+1] = alist[i]
            self.size = len(alist)
        for j in range(self.parent(self.size), 0, -1):
            self.perc_down(j)


    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while self.parent(i) > 0:
            if self.heap[i] > self.heap[self.parent(i)]:
                temp = self.heap[i]
                self.heap[i] = self.heap[self.parent(i)]
                self.heap[self.parent(i)] = temp
            i = self.parent(i)

    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while 2*i <= self.size:
            left = 2*i 
            right = 2*i + 1
            if 2*i == self.size:
                choose = left
            else:
                if self.heap[left] > self.heap[right]:
                    choose = left
                else:
                    choose = right

            if self.heap[i] < self.heap[choose]:
                temp = self.heap[i]
                self.heap[i] = self.heap[choose]
                self.heap[choose] = temp
            i = choose

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if self.is_full():
            return False
        self.size += 1
        self.heap[self.size] = item
        i = self.size
        if i > 1:
            self.perc_up(i)
        return True
        
    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        if self.is_empty():
            return None
        return self.heap[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        returnvalue = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        self.perc_down(1)
        
        return returnvalue

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        returnlist = []
        for i in self.heap:
            if i != None:
                returnlist.append(i)
        return returnlist


    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        if self.size == 0:
            return True
        return False

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        if self.size == self.capacity:
            return True
        return False
        
    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size
        
    def parent(self,index):
        return index//2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        self.build_heap(alist)
        while not self.is_empty():
            for i in range(len(alist)-1,-1,-1):
                alist[i] = self.dequeue()

