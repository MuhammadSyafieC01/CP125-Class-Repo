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

    f1 = open(file1,"r")
    # TODO: Implement this function
    f2 = open(file2,"r")
    f3 = open(file3,"a")


    name1 = f1.readlines()
    name2 = f2.readlines()
    name3 = list(set(name1)|set(name2))
    

    print(name3)

    for i in name3:
        f3.write(name3[1])



    f1.close()
    f2.close()
    f3.close()