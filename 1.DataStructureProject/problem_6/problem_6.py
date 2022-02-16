class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

    def __repr__(self):
        return str(self.value)

class Linkedlist:
    def __init__(self):
        self.head=None

    def __str__(self):
        cur_head=self.head
        out_string=""
        while cur_head:
            out_string+=str(cur_head.value)+"->"
            cur_head=cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head=Node(value)
            return
        node=self.head
        while node.next:
            node=node.next

        node.next=Node(value)

    def size(self):
        size=0
        node=self.head
        while node:
            size+=1
            node=node.next

        return size

def union(llist_1, llist_2):
    """
    Returns the union of two linked lists.
    """
    if llist_1.head==None:
        if llist_2.head==None:
            return None
        else:
            return llist_2
    else:
        if llist_2.head==None:
            return llist_1
        else:
            dict_=dict()
            llist_combine=Linkedlist()
            head_1=llist_1.head
            while head_1:
                if head_1.value not in dict_:
                    dict_[head_1.value]=1
                    llist_combine.append(head_1)
                head_1=head_1.next
            head_2=llist_2.head
            while head_2:
                if head_2.value not in dict_:
                    dict_[head_2.value]=1
                    llist_combine.append(head_2)
                head_2=head_2.next
            return llist_combine

def intersection(llist_1, llist_2):
    """
    Returns the intersection of the two linked lists.
    """
    if llist_1.head==None or llist_2.head==None:
        return None
    else:
        dict_=dict()
        llist_inter=Linkedlist()
        head_1=llist_1.head
        while head_1:
            if head_1.value not in dict_:
                dict_[head_1.value]=1
            head_1=head_1.next
        head_2=llist_2.head
        while head_2:
            if head_2.value in dict_ and dict_[head_2.value]==1:
                llist_inter.append(head_2)
                dict_[head_2.value]+=1
            head_2=head_2.next
        if llist_inter.head==None:
            return None
        return llist_inter

#Test
#1
print('Test1')
linked_list_1=Linkedlist()
linked_list_2=Linkedlist()

element_1=[3,2,4,35,6,65,6,4,3,21]
element_2=[6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2)) #Should return 3->2->4->35->6->65->21->32->9->1->11->
print(intersection(linked_list_1,linked_list_2)) # Should return 6->4->21->
print('Test1 done.')
print('-----------------------------------------------------------------')

#2
print('Test2')
linked_list_3=Linkedlist()
linked_list_4=Linkedlist()

element_1=[3,2,4,35,6,65,6,4,3,23]
element_2=[1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4)) # Should return 3->2->4->35->6->65->23->1->7->8->9->11->21->
print(intersection(linked_list_3,linked_list_4)) # Should return None.
print('Test2 done.')
print('-----------------------------------------------------------------')

#3
print('Test3')
linked_list_5=Linkedlist()
linked_list_6=Linkedlist()

element_1=[]
element_2=[1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5,linked_list_6)) # Should return 1->7->8->9->11->21->1->
print(intersection(linked_list_5,linked_list_6)) # Should return None.
print('Test3 done.')
print('-----------------------------------------------------------------')

#4
print('Test4: Both lists are empty')
linked_list_7=Linkedlist()
linked_list_8=Linkedlist()

element_1=[]
element_2=[]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7,linked_list_8)) # Should return None.
print(intersection(linked_list_7,linked_list_8)) # Should return None.
print('Test4 done.')
print('-----------------------------------------------------------------')
