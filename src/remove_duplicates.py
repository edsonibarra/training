def remove_duplicates(s):
    l=[]
    for c in s:
        if l:
            if l[-1]==c:
                l.pop()
            else:
                l.append(c)
        else:
            l.append(c)
    return "".join(l)
print(remove_duplicates('abbaca'))