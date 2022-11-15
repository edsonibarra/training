def rotate_str(s,goal):
    i = 0
    while i < len(s):
        new_str = s[1:] + s[0]
        if new_str == goal:
            return True
        s = new_str
        i+=1
