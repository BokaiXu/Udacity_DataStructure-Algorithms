#### Explanation: 
I fill the ipynb according to the procedure on the Udacity workspace.
#### Time complexity:
TrieNode.insert() is O(1) since it use dictionary.    
TrieNode.suffixes() is O(n) since it traverse the nodes.  
TrieNode.init() is O(1) since it set value to self.
Trie.init() is O(1) since it set value to self.
Trie.add() is O(n) since it traverse the nodes.      
Trie.exists() is O(n) since it traverse the nodes.     
Trie.find_prefix() is O(n) since it traverse the nodes.
#### Space complexity:
TrieNode.init() is O(1) since it set value to self.
TrieNode.insert() is O(1) since it use dictionary.  
TrieNode.suffixes(# of word * length of word).
Trie: add() is O(1) since it adds one new element every time.
Trie.exists() is O(1) since it does not need extra space.
Trie.find_prefix() is O(1) since it does not need extra space.
Trie.init() is O(1) since it set value to self.