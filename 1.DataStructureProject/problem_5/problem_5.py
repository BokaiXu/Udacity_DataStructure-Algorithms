import time
import hashlib

class Block:
    # This is the element for block chain.
    def __init__(self,data,timestamp=None, prev_hash=0):
        self.data=data
        if timestamp==None:
            self.timestamp=self.time_GMT()
        else:
            self.timestamp=timestamp
        self.SHA=self.SHA_generator(self.data)
        self.prev_hash=prev_hash
        self.next=None

    def time_GMT(self):
        # Record time in GMT.
        gmt = time.gmtime(time.time())
        timestamp=str(gmt.tm_hour)+':'+str(gmt.tm_min)+' '+str(gmt.tm_mon)+'/'+str(gmt.tm_mday)+'/'+str(gmt.tm_year)
        return timestamp

    def SHA_generator(self,data):
        # Generator a SHA according to data in the block.
        sha = hashlib.sha256()
        try:
            hash_str = data.encode('utf-8')
            sha.update(hash_str)
            return sha.hexdigest()
        except:
            hash_str = 'None'.encode('utf-8')
            sha.update(hash_str)
            return sha.hexdigest()

class Blockchain:
    # This is the blockchain data strucrue.
    def __init__(self,data=None,timestamp=None,prev_hash=0):
        self.num_elements=1
        self.head=Block(data,timestamp,prev_hash)
        self.tail=self.head

    def size(self):
        # Return the size of the blockchain.
        return self.num_elements

    def add(self,data,timestamp=None,prev_hash=0):
        # Function to add a block in the end of the chain.
        if self.head==None:
            self.head=Block(data,timestamp,prev_hash)
            self.tail=self.head
            self.num_elements=1
        else:
            temp_hash=self.tail.SHA
            self.tail.next=Block(data,timestamp,prev_hash)
            self.tail=self.tail.next
            self.num_elements+=1
            self.tail.prev_hash=temp_hash

    def search(self,SHA):
        # According to the SHA to find the related data.
        if self.head==None:
            return None
        else:
            node=self.head
            while node.next:
                if node.SHA==SHA:
                    return node.data
                node=node.next
            return None

    def pop(self):
        # Remove the latest block and return the SHA.
        if self.head==None:
            return None
        elif self.head==self.tail:
            result=self.head.SHA
            self.head=None
            self.tail=None
            self.num_elements=0
            return result
        else:
            result=self.tail.SHA
            node=self.head
            while node.next:
                if node.next==self.tail:
                    break
                node=node.next
            self.tail=node
            self.tail.next=None
            self.num_elements-=1
        return result

    def __repr__(self):
        # Return all the SHAa in the blockchain.
        if self.head==None:
            return 'Empty block chain!'
        node=self.head
        SHA_result=''
        while node:
            result='Block SHA: {}'.format(node.SHA)
            SHA_result+=result
            SHA_result+='\n'
            node=node.next
        return SHA_result

#Test
#1
print('Test1')
blockchain_test=Blockchain('block1')
blockchain_test.add('block2')
blockchain_test.add('block3')
blockchain_test.add('block4')
blockchain_test.add('block5')
print('Size of the block chain: {}'.format(blockchain_test.size())) # Should return 5
print('SHA of the blockchain {}'.format(blockchain_test)) # Should return
# Block SHA: 9a59c5f8229aab55e9f855173ef94485aab8497eea0588f365c871d6d0561722
# Block SHA: 6d0b07ee773591f2a1b492d3ca65afdefc90e1cadfcc542a74048bb0ae7daa27
# Block SHA: 7e56ddaff5ff44d9e1732b1fd138a2057df045b163385068988554f72047e272
# Block SHA: 215008ba416eb06b8cfd53814660a43255e4ccc8703080af501ea0eaf7b7fdea
# Block SHA: 2e134675975ce520a5b2f59a4a13846a399d73c3152647a6c1757842f8864f0b
print('Test1 done.')
print('---------------------------------------------------------------------------------------------------')

#2
print('Test2: Create an empty blockchain')
blockchain_test=Blockchain()
print('Test2 done.')
print('---------------------------------------------------------------------------------------------------')

#3
print('Test3: Create different blocks with the same timestamp')
blockchain3=Blockchain('1',timestamp=1)
blockchain3.add('2',timestamp=1)
blockchain3.add('3',timestamp=1)
print('Test3 done.')
print('---------------------------------------------------------------------------------------------------')
