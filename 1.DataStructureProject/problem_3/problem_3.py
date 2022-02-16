from collections import defaultdict
import sys

class Tree_node:
    def __init__(self,value,left=None,right=None,name=None):
        self.value=value
        self.left=left
        self.right=right
        self.name=name

class Queue_node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def add(self,node):
        if self.head==None:
            self.head=node
            self.tail=node
            return
        elif self.head.value.value>=node.value.value:
            node.next=self.head
            self.head=node
            return
        elif self.tail.value.value<=node.value.value:
            self.tail.next=node
            self.tail=self.tail.next
            return
        else:
            pointer=self.head
            while pointer.next:
                if node.value.value<pointer.next.value.value:
                    temp=pointer.next
                    pointer.next=node
                    node.next=temp
                    return
                pointer=pointer.next
    def pop(self):
        if self.head==None:
            return None
        else:
            node=self.head
            self.head=self.head.next
            return node

def count_freq(string):
    """
    This function count the frequency of the word in a string and return a dictionary.
    """
    dict_=defaultdict(int)
    for char in string:
        dict_[char]+=1
    return dict_

def tree_generator(data):
    dict1=count_freq(data)    
    queue=Queue()
    for key,value in dict1.items():
        queue.add(Queue_node(Tree_node(value=value,name=key)))
    while queue.head:
        left=queue.pop()
        right=queue.pop()
        if right==None:
            tree_headnode=left.value
            break
        else:
            combine_value=left.value.value+right.value.value
            combine_tree_node=Tree_node(combine_value,left.value,right.value)
            queue.add(Queue_node(combine_tree_node))
    if len(dict1)==1:
        tree_headnode.left=Tree_node(value=None,name=tree_headnode.name)
        return tree_headnode
    else:
        return tree_headnode

def encoder(root):
    """
    This function loop the tree and generate a dictionary that store the word and the related code.
    """
    def construct_paths(root,path=''):
        if root:
            if root.left==None and root.right==None:
                paths[root.name]=path
            else:
                construct_paths(root.left,path+'0')
                construct_paths(root.right,path+'1')
    paths=dict()
    construct_paths(root,'')
    return paths

def huffman_encoding(data):
    """
    This function convert the data into the encoded data and return the encoded data and root of the tree.
    """
    if data=='':
        print ('No data to encode!')
        return None,None
    encoded_data=''
    root=tree_generator(data)
    code_dict=encoder(root)
    for i in data:
        encoded_data+=code_dict[i]
    return encoded_data, root

def huffman_decoding(data,tree):
    """
    This function convert the encoded data into the decoded data.
    """
    if data==None and tree==None:
        print ('No data to decode!')
        return None
    decoded_data=''
    node=tree
    while len(data)>0:
        word=data[0]
        data=data[1:]
        if word=='0':
            node=node.left
            if node.name!=None:
                decoded_data+=node.name
                node=tree
        else:
            node=node.right
            if node.name!=None:
                decoded_data+=node.name
                node=tree
    return decoded_data

if __name__ == "__main__":
    #Test1
    print('Test1')

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # Should return 69
    print ("The content of the data is: {}\n".format(a_great_sentence)) # Should return The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # Should return 36
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # Should return 0001001010111000001110010111101111011111110100010101111100111000100101

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # Should return 69
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # Should return The bird is the word
    print('Test1 done.')
    print('---------------------------------------------------------------------------')

    #Test2
    print('Test2')

    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # Should return 49
    print ("The content of the data is: {}\n".format(a_great_sentence)) # Should return nothing

    encoded_data, tree = huffman_encoding(a_great_sentence) # returns No data to encode!

    decoded_data = huffman_decoding(encoded_data, tree) # returns No data to decode!

    print('Test2 done.')
    print('---------------------------------------------------------------------------')

    #Test3
    print('Test3')

    a_great_sentence = "AAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # Should return 52
    print ("The content of the data is: {}\n".format(a_great_sentence)) # Should return AAA!

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # Should return 24
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # Should return 000

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # Should return 52
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # Should AAA!
    print('Test3 done.')
    print('---------------------------------------------------------------------------')
