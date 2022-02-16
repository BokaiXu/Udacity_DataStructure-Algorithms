class Node:
    # Node for the double linked list.
    def __init__(self,key, value):
        self.key=key
        self.value=value
        self.next=None
        self.previous=None

class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        if capacity<=0:
            print( 'Negative Input!')
            return
        if capacity>50:
            print('Capacity is too high!')
            return
        self.num_elements=0 # Keep track of the number of elements in the list.
        self.capacity=capacity
        self.dict_=dict()
        self.head=Node(0,0)
        self.tail=Node(0,0)
        # Link the head and tail nodes.
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict_.keys():
            # if the key is in the hash map, then find the node. Delete the node and put it in the latest position.
            node=self.dict_[key]
            value=node.value
            self.delete_node(node)
            self.insert_node(node)
            return value
        else:
            return -1

    def put(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.dict_.keys():
            # if the key is in the hash map, then find the node. Delete the node and put it in the latest position.
            node=self.dict_.keys[key]
            self.delete_node(node)
            self.insert_node(node)
            return
        else:
            # If the key is not in the hash map, create a new node.
            self.dict_[key]=Node(key,value)
            node=self.dict_[key]
            if self.num_elements<self.capacity:
                # If the linked list in not full, insert the new node.
                self.insert_node(node)
                self.num_elements+=1
                return
            else:
                # If the linked list is full, delete the oldest node from the list and the key from the hash map.
                old_node=self.head.next
                old_key=old_node.key
                del self.dict_[old_key]
                self.delete_node(old_node)
                # Insert the new node.
                self.insert_node(node)
                return
    def insert_node(self,node):
        # Method for insert a node to the linked list in O(1).
        node.next=self.tail
        self.tail.prev.next=node
        node.prev=self.tail.prev
        self.tail.prev=node

    def delete_node(self,node):
        # Method for delete a node in the linked list in O(1).
        node.prev.next=node.next
        node.next.prev=node.prev

# Test
#1 Test code provided by Udacity
print('test_1')
our_cache = LRU_Cache(5)
our_cache.put(1, 1);
our_cache.put(2, 2);
our_cache.put(3, 3);
our_cache.put(4, 4);
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
our_cache.put(5, 5)
our_cache.put(6, 6)
print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print('-----------------')

#2 Getting the same value over and over again to see if the program works & Getting only invalid values
print('test_2')
our_cache2 = LRU_Cache(3)
our_cache2.put(1, 1);
our_cache2.put(2, 2);
our_cache2.put(3, 3);
print(our_cache2.get(1))       # returns 1
print(our_cache2.get(1))       # returns 1
print(our_cache2.get(1))      # returns 1 
print(our_cache2.get(4))      # returns -1
print('-----------------')

#3 Adding cases where the input is negative, or high capacity.
print('test_3')
our_cache3 = LRU_Cache(-1) # returns Negative Input!
our_cache4 = LRU_Cache(100)# returns Capacity is too high!
our_cache5 = LRU_Cache()# returns nothing
print('-----------------')
