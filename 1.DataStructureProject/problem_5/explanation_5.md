For this question, I used double linked list to simulate the structure of block chain.
The time complexity and space complexity of the size() function is O(1).
The time complexity of the add() function is O(1) since it just add the new node to the tail. The space complexity is O(size of the blockchain)=O(n).
The time complexity of the search() function is O(n) since it has to traverse the blockchain. The space complexity is O(size of the blockchain)=O(n).
The time complexity of the pop() function is O(n) since it has to traverse the blockchain. The space complexity is O(size of the blockchain)=O(n).
The time complexity of the __repr__() function is O(n) since it has to traverse the blockchain. The space complexity is O(size of the blockchain)=O(n).