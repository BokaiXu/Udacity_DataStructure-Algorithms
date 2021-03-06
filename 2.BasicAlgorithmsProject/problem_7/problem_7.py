# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root=RouteTrieNode(handler)
        self.handler=handler

    def insert(self, url, handler=None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node=self.root
        for i in url:
            if i not in node.children:
                node.insert(i)
            node=node.children[i]
        node.handler=handler

    def find(self, url):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node=self.root
        for i in url:
            if i not in node.children:
                return None
            node=node.children[i]
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children={}
        self.handler=handler
    def insert(self,url,handler=None):
        # Insert the node as before
        self.children[url]=RouteTrieNode(handler)

# The Router class will wrap the Trie and handler
class Router:
    def __init__(self,handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root=RouteTrie(handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        node=self.root
        path_list=self.split_path(path)
        node.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        node=self.root
        path_list=self.split_path(path)
        if path_list==['']:
            return node.handler
        if node.find(path_list)==None:
            return 'not found handler'
        else:
            return node.find(path_list)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path=path.split('/')
        path_list=path[1:]
        return path_list

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
