'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Computes the cosine similarity of dictionaries vec1 and vec2
    '''
    #Firstly, we need to find matching keys between vec1 and vec2
    matching = (set(vec1.keys()).intersection(set(vec2.keys())))

    #Solve for the numerator of the equation
    numerator = 0
    for i in matching:
        numerator += (vec1.get(i) * vec2.get(i))

    #Solve for the denominator of the equation
    sum_1, sum_2 = 0, 0
    for values in vec1.values():
        sum_1 += values**2
    for values in vec2.values():
        sum_2 += values**2
    denominator = math.sqrt(sum_1 * sum_2)

    #Solve for cosine similarity
    return (numerator/denominator)

def build_semantic_descriptors(sentences):
    pass

def build_semantic_descriptors_from_files(filenames):
    pass

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass

if __name__ == "__main__":
    print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))