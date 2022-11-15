def majority_element(nums):
    n1 = len(nums)//2
    d = {}
    m = 0
    max_v = 0
    
    for n in nums:
        d[n] = d.get(n,0) + 1

    for k,v in d.items():
        print('k',k,'v',v)
        if v > n1:
            m = k
    return m