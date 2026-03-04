# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, file3):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """

    """f1 = open(file1,"r")
    # TODO: Implement this function
    f2 = open(file2,"r")
    

    set1 = set(f1.readlines())
    set2 = set(f2.readlines())

    listfinal = list(set1 | set2)
    listfinal.sort()
    print(listfinal)
  
    

    f1.close()
    f2.close()"""
    print(file1)
    print(file2)
    print(file3)

    final = set(file1) | set(file2)
    print(final)



list1 = [1,2,3,4]
list2 = [3,4,5,6,7,8]
list3 = []

# Test your code here
result = merge_lists(list1,list2,list3)
print(f"Unique names: {result}")
