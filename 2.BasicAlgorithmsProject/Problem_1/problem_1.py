def find_root(num):
    """
    This function find the square root of the number. The result is round to floor value.
    input: number.
    output: Square root of the number. Floor value.
    """
    if num<0:
        return 'Negative number input!'
    if num<=1:
        return num
    left=1
    right=num
    middle=(left+right)//2
    while left+1<right:
        if middle*middle>num:
            right=middle
        elif middle*middle<num:
            left=middle
        else:
            return middle
        middle=(left+right)//2
    if middle*middle<num:
        return middle
    else:
        return middle-1

#Test
print ("Pass" if  (3 == find_root(9)) else "Fail")
print ("Pass" if  (0 == find_root(0)) else "Fail")
print ("Pass" if  (4 == find_root(16)) else "Fail")
print ("Pass" if  (1 == find_root(1)) else "Fail")
print ("Pass" if  (5 == find_root(27)) else "Fail")
print ("Pass" if  ('Negative number input!' == find_root(-5)) else "Fail")
print ("Pass" if  (99 == find_root(9999)) else "Fail")
