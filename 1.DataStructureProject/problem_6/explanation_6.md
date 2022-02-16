For the union() function, I used a dictionary to store the values of the two linked lists. Store the value of the nodes as key. Then put the keys in a new likned list. The time complexity of the function is O(len(linked list1)+len(linked list2))=O(n). The space complexity is O(2*len(linked list1)+2*len(linked list2))=O(n) since I have to use a dictionary to store the linked lists.

For the intersection() function, I used a dictionary to store the values of the first linked list. Then traverse the second linked list to see whether the node value has been stored in the dictionary. If true then add the value to the new linked list. The time complexity of the function is O(len(linked list1)+len(linked list2))=O(n). The space complexity is O(len(linked list1))=O(n) since I have to use a dictionary to store the same value in the linked lists.