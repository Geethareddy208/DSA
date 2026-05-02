class maxHeap:

    def __init__(self):
        # Initialize your data members
        self.heap=[]
        

    # Insert x into the heap
    def push(self, x: int):
        # code here
        self.heap.append(x)
        self.heapify_up(len(self.heap)-1)


    # Remove the top (maximum) element
    def pop(self):
        # code here
        if not self.heap:
            return -1
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root


    # Return the top element or -1 if empty
    def peek(self) -> int:
        # code here
        if not self.heap:
            return -1
        return self.heap[0]


    # Return the number of elements in the heap
    def size(self) -> int:
        # code here
        return len(self.heap)
    
    
    def heapify_up(self,i):
        parent=(i-1)//2
        if i>0 and self.heap[parent]<self.heap[i]:
            self.heap[parent],self.heap[i]=self.heap[i],self.heap[parent]
            self.heapify_up(parent)
    
    
    
    def heapify_down(self,i):
        n=len(self.heap)
        largest=i
        left=2*i+1
        right=2*i+2
        if left<n and self.heap[left]>self.heap[largest]:
            largest=left
        if right<n and self.heap[right]>self.heap[largest]:
            largest=right
        if largest!=i:
            self.heap[i],self.heap[largest]=self.heap[largest],self.heap[i]
            self.heapify_down(largest)
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        