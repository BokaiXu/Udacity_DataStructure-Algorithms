def find_max_min(array):
    if len(array)==0:
        return 'Array is empty!'
    if len(array)==1:
        return(array[0],array[0])
    max_index=0
    min_index=0
    for index, value in enumerate(array):
        if value>array[max_index]:
            max_index=index
        if value<array[min_index]:
            min_index=index
    return (array[max_index],array[min_index])

#Test
array=[10,5,0,-3,3,45,13,6]
print(find_max_min(array)) # Should print (45,-3)

array=[100,93,-234,34,9,0,34,53,-34]
print(find_max_min(array)) # Should print(100,-234)

array=[1]
print(find_max_min(array)) # Should print(1,1)

array=[]
print(find_max_min(array)) # Should return Array is empty!

array=[0,0,0,0,0,0]
print(find_max_min(array)) # Should return (0,0)
