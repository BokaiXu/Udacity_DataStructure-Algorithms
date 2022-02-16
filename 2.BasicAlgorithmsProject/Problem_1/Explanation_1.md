#### Explanation:    
We could use binary search to find the value. Find the middle value between 1 and the number, then compare the value of middle times middle with the number. If the value of middle times middle is larger than the number, recursively run the find_root function to check the middle between 1 and the previous middle. If the value of the middle times middle is smaller than the number, recursively run the find_root function to check the middle between the previous middle and the number. If the value of the middle times middle is equal to the number, return the middle. Finally, if right value minus left value is equal to one, compare the value of middle times middle and number it self. 
#### Time complexity:     
Since it is kind of a binary search, it will use O(log(n)) time complexity.     
#### Space complexity:
O(1) since no other extra space used.    