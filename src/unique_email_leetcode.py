# O(n) Time
# O(n) Space

def unique_email(emails):
    valid = []
    for email in emails:
        fp = email.split("@")[0].replace(".","") 
        sp = email.split("@")[1]
        if '+' in fp:
            fp = fp[:fp.find('+')]
        e = fp+"@"+sp
        if e not in valid:
            valid.append(e)
    
    return len(valid)
