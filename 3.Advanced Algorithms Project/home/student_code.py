def calculate_distance(node1,node2):
    # Since the map is 2d with points. I decided to use Euclidean distance.
    # We could also try other type of distances like Manhattan distance. 
    # Or try to calculate different types of distance and use an average value.
    import math
    distance=math.sqrt((node1[0]-node2[0])*(node1[0]-node2[0])+(node1[1]-node2[1])*(node1[1]-node2[1]))
    return distance

def shortest_path(M,start,goal):
    # Edge case
    if start==goal:
        return [start]
    from queue import PriorityQueue
    # let openList equal empty list of nodes
    # let openlist queus as priority queue to store nodes with distance_f
    open_list_queue=PriorityQueue()
    open_list=[]
    # let map_dict to store the node with distance_g
    map_dict={}
    # let map_dict_2 to store the previous node of current node
    map_dict_2={}
    map_dict[start]=0
    map_dict_2[start]=None
    # let closedList equal empty list of nodes
    closed_list=[]
    # put startNode on the openList (leave it's f at zero)
    open_list_queue.put((0,start))
    open_list.append(start)
    # while openList is not empty
    while not open_list_queue.empty():
        # let currentNode equal the node with the least f value
        # remove currentNode from the openList
        current_node=open_list_queue.get()
        # add currentNode to the closedList
        closed_list.append(current_node[1])
        # if currentNode is the goal
        if current_node[1]==goal:
            # You've found the exit!
            # backverse map_dict_2 to build the path
            result=[goal]
            node_search=map_dict_2[goal]
            while node_search!=start:
                result.append(node_search)
                node_search=map_dict_2[node_search]
            result.append(start)
            break
        # let children of the currentNode equal the adjacent nodes
        # for each child in the children
        for node in M.roads[current_node[1]]:
            # if child is in the closedList
            if node in closed_list:
                # continue to beginning of for loop
                continue
            # child.g = currentNode.g + distance b/w child and current
            distance_g=map_dict[current_node[1]]+calculate_distance(M.intersections[current_node[1]],M.intersections[node])
            # child.h = distance from child to end
            distance_h=calculate_distance(M.intersections[node],M.intersections[goal])
            # child.f = child.g + child.h
            distance_f=distance_h+distance_g
            # if the child node is not in map_dict or the distance_g is smaller than the one in map_dict 
            # then undate the value in the map_dict
            if node not in map_dict or distance_g<map_dict[node]:
                map_dict[node]=distance_g
                map_dict_2[node]=current_node[1]
            # add the child to the openList
            open_list.append(node)
            open_list_queue.put((distance_f,node))
    
    result.reverse()
    return result