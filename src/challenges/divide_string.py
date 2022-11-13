def divide_string(s, k, fill):
    l = len(s)
    is_evenly_divisible = True if l%k == 0 else False
    ans = []
    
    if not is_evenly_divisible:
        remaining = l % k
        left = k - remaining
        
        for _ in range(left):
            s+=fill

        i=0
        while i <= len(s)-k:
            substring = s[i:i+k]
            ans.append(substring)
            i+=k
    else:
        remaining = l % k
        left = k - remaining
        for _ in range(left):
            s+=fill

        i=0
        while i<len(s)-k:
            substring = s[i:i+k]
            print(substring)
            ans.append(substring)
            i+=k
            
    return ans
