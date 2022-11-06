def large_group_positions(s):
    
    len_large_group = 3
    
    visited_chars = list()
    
    ans = []
    
    start = 0
    end = 1
    
    current_chars_count = 0
    
    while end < len(s):
        
        while s[start] == s[end]:
            current_chars_count += 1
            end += 1

        if current_chars_count >= len_large_group:
            ans.append([start,end - 1])
            current_chars_count = 0
    
        start = end
        end += 1
    
    print(ans)
    return ans

print(large_group_positions("abbxxxxzzffy"))
        
        
