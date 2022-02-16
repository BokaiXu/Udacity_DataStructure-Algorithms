import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
    else:
        try:
            file_list=os.listdir(path)
        except:
            return 'Invalid path!'
        result=[]
        for file in file_list:
            path_next=os.path.join(path,file)
            sub_result=find_files(suffix,path_next)
            if sub_result!=None:
                result+=sub_result
        return result

def main():
    print(find_files('.c', './testdir'))
    #['./testdir\\subdir1\\a.c', './testdir\\subdir3\\subsubdir1\\b.c', './testdir\\subdir5\\a.c', './testdir\\t1.c']
    print('test1 done')
    print('------------------------')
    print(find_files('.c', './d'))
    # returns Invalid path!
    print('test2 [Invalid Input Path] done')
    print('------------------------')
    print(find_files('.c', './testdir/subdir2'))
    # returns []
    print('test3 [No files found for the given extension] done')
    print('------------------------')

if __name__=='__main__':
    main()
