class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # new_s = 'abcd' -> 'dcba'
        # "ab-cd"
        # cur (s) = a
        # result (new_s) = d
        # cur = b
        # result = dc
        # cur = - (is not a letter)
        # result = dc + cur
        # cur = c
        # result = dc-b
        # cur = a
        # result = dc-ba


        # Get a new string containing only letters from "s" and reverse it.    
        only_letters_string = "".join([c for c in s if c.isalpha()])[::-1]

        i = 0 # This is for s index 
        j = 0 # This is for only_letters_string index. Since we deleted all non-alpha char the length of both is not the same
        result_string = '' # To store the result
        while i < len(s):
            if s[i].isalpha():
                # If the current character is apha we'll concatenate character at position j to out result string and increment j
                # Since we already reverse it, we do not need to do anything else
                result_string += only_letters_string[j]
                j += 1
            else:
                # Otherwise concatenate the non-alpha char from s
                result_string += s[i]
            i += 1
        
        return result_string
