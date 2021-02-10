def long_repeat(line):

    long_count = 0
    cur_char = ""
    cur_count = 0

    """
    Students might also use a range for loop, e.g.:

    for in in range(len(text)):

    In which case they'll need to access the current character
    via the [] index operator.
    """

    for char in line:

        if char == cur_char:
            cur_count += 1
        else:
            cur_char = char
            cur_count = 1
        
        if cur_count > long_count:
            long_count = cur_count
    
    return long_count