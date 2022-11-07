def group_anagrams():
    """Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    
    pass


def get_chars(word):
    """Return a dict with the letters of the word and the count
    of the letters as value

    Args:
        word : word to get the chars from

    Returns:
        dict: letters
    """
    d = {}
    for c in word:
        d[c] = d.get(c,0) + 1
    return d