#### Time complexity:
For RouteTrie class: insert() function is O(n); find() function is O(n). Since the functions need to traverse the RouteTrie. init() is O(1) since it set value to self.  
For RouteTrieNode class: insert() function is O(1) since it used python dictionary(hashmap).  init() is O(1) since it set value to self.
For Router class: lookup() function is O(n) since it utlized find() function from RouteTrie class; add_handler() function is also O(n) since it used the split_path() function and insert() function; split_path function is also O(n) since this is the python built in function. init() is O(1) since it set value to self.     

#### Space complexity:
RouteTrieNode: insert() O(n) where n is the length of the route. init() is O(1) since it set value to self.
RouteTrie: Both functions are O(1) since no extra space was used. init() is O(1) since it set value to self. 
Router:add_handler() function is O(1) since it adds one hander every time. lookup() function is O(1) since it does not use extra space. split_path() function is O(length of the string/link) since it uses the python built in split function. init() is O(1) since it set value to self. 