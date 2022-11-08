# def check_almost_equivalent(word1, word2):

#     d1 = {}
#     for c in word1:
#         d1[c] = d1.get(c,0)+1
    
#     d2 = {}
    
#     for c in word2:
#         d2[c] = d2.get(c,0)+1
    
#     for c in d1:
#         if c in d2 and abs(d1[c] - d2[c]) > 3:
#             return False
#         elif  c not in d2 and d1[c] > 3:
#             return False
        
#     for c in d2:
#         if c in d1 and abs(d1[c] - d2[c]) > 3:
#             return False
#         elif  c not in d1 and d2[c] > 3:
#             return False
        
#     return True


def check_almost_equivalent(word1, word2):
    """Optimized version of the above
    """
    
    d1 = {}
    for c in word1:
        d1[c] = d1.get(c,0)+1
    for c in word2:
        d1[c] = d1.get(c,0)-1
    values = d1.values()
    for n in values:
        if abs(n) > 3:
            return False
    return True
        

# print(check_almost_equivalent('aaaa','bccb'))
# print(check_almost_equivalent('abcdeef','abaaacc'))
# print(check_almost_equivalent('cccddabba','babababab'))

# print(check_almost_equivalent('aaaa','aaaa'))

print(check_almost_equivalent('zzzyyy','iiiiii'))
print(check_almost_equivalent('abcdeef','abaaacc'))


            
