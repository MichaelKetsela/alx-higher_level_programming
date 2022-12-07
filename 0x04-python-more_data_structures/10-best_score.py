#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    score = list(a_dictionary.keys())[0]
    name = a_dictionary[score]
    for k, v in a_dictionary.items():
        if v > name:
            name = v
            score = k
    return (score)
