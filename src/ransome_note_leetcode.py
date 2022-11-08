# def ransome_note(ransome_note, magazine):

#     lrn = get_dict(magazine)

#     new_lrn = substract_values(lrn, ransome_note)

#     for k,v in new_lrn.items():
#         if v <= 0:
#             return False

#     return True

# def get_dict(magazine):
#     print("Starting get_dict")
#     lrn = {}
#     for c in magazine:
#        lrn[c] = lrn.get(c,0)+1
#     #print(lrn)
#     print("Finished get_dict, result: ", lrn)
#     return lrn

# def substract_values(lrn,ransome_note):
#     print("Starting process substract_values")
#     for c in ransome_note:
#         print("Current value of c: ", c)
#         if c not in lrn:
#             print('not in lrn', c)
#             return False
#         elif c in lrn:
#             print(f"Substracting value of c, current {lrn[c]}")
#             lrn[c] -= 1
#             print(f"Substracted value, result of c", lrn[c])

#     print("Finishing process substract_values")
#     return lrn
# print(ransome_note("aa","aab"))


def ransome_note(ransome_note_str, magazine):

    index_ransome_note = 0
    index_magazine = 0

    sorted_ransome_note = sorted(ransome_note_str)
    sorted_magazine = sorted(magazine)

    # success = len(ransome_note) - 1

    while index_ransome_note < len(ransome_note_str):

        if sorted_magazine[index_magazine] == sorted_ransome_note[index_ransome_note]:
            index_ransome_note += 1
            index_magazine += 1
        else:
            index_ransome_note += 1
    print(f"index magazine: {index_magazine}\nindex ransome note: {index_ransome_note}")
    if index_ransome_note == index_magazine:
        return True
    return False
