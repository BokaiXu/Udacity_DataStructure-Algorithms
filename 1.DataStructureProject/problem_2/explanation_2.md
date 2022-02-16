In this question I need to look for a certain type of file in a folder.
To look for subfolders in the folder and subsubfolders in subfolders, etc, I think it will be good to use recursion to do it.
The idea is write a function to see if the folder contains the certain type of file and call the function again to check the subfolder.

The time complexity is O(depth * average number of folders in each level).
Since we use recursion, the space complexity is O(depth).