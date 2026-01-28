def manage_roster(enrolled, drop_requests, waitlist):
    """
    Processes student drop requests and adds from waitlist if needed.
    
    Args:
        enrolled: Set of currently enrolled student names
        drop_requests: List of student names requesting to drop
        waitlist: Set of students on the waitlist
    
    Returns:
        int: Count of final enrolled students
    """
    setenrolled = set(enrolled)
    setdroprequests = set(drop_requests)
    setwaitlist = set(waitlist)
    newenrolled = enrolled - setdroprequests
    if len(newenrolled) < 5:
        needtoadd = 7 - len(setdroprequests)

    print(newenrolled,needtoadd)

manage_roster({"Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "George"}, ["Alice", "Charlie", "Diana", "Eva"], {"Henry", "Iris", "Jack"})