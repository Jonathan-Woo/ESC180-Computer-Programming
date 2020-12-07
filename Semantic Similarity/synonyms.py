'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math, copy


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
    '''Returns a dictionary whose keys are words in the list
    sentences and values are the semantic descriptor of the words
    '''
    semantic_descriptors = {}
    #Loop through sentences once. However, we have to loop through
    #each sublist the length of the sublist times
    for sublist in sentences:
        full_sentence_copy = copy.deepcopy(sublist)
        full_sentence = copy.deepcopy(sublist)
        for word in full_sentence:
            full_sentence_copy.remove(word)
            for word_to_update in full_sentence_copy:
                #Make a dictionary entry for each word if it does not exist
                #already
                if word_to_update not in semantic_descriptors:
                    semantic_descriptors[word_to_update] = {}

                #Once we know that the word to update is in the dictionary
                #semantic_descriptors, we need to check if the word we want
                #to update (word) exists in that sub-dictionary yet
                #if it does, then increment it by 1. If not, set it to 1
                if word in semantic_descriptors[word_to_update]:
                    semantic_descriptors[word_to_update][word] += 1
                else:
                    semantic_descriptors[word_to_update][word] = 1

            #After going through each item in the sublist, reset the sublist
            #to the full sentence and remove the next item
            full_sentence_copy = copy.deepcopy(full_sentence)
    return semantic_descriptors

def build_semantic_descriptors_from_files(filenames):
    '''Creates a dictionary of semantic descriptors for all of the
    sentences in each file.
    '''
    sentences = []
    separated_sentences = []
    #for each file, break up the sentences and append the separated words to
    #a list sentences
    for filename in range(len(filenames)):
        lines = open(filenames[filename], "r", encoding="latin1").read().split("\n")

        #Now that we have all the lines of the text in a list, we must join the
        #lists as a single string.
        text = ""
        for item in lines:
            text += item + " "
        text = text[:len(text)-1]

        #Convert all punctuation types to "." so that we only have to
        #split once
        text.replace("!", ".")
        text.replace("?", ".")
        sentences = text.split(".")
        sentences = remove_empties(sentences)
        for item in sentences:
            #We convert all punctuation to spaces so that we only have to
            #split once.
            item.replace(",", " ")
            item.replace("-", " ")
            item.replace(":", " ")
            item.replace(";", " ")
            separated_sentences.append(remove_empties(item.split(" ")))

    return build_semantic_descriptors(separated_sentences)

def remove_empties(list):
    '''Helper function that removes the empty elements of a list list
    '''
    for item in list:
        if item == '':
            list.remove('')
    return list

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''Determines the word in the list choices that has the closest semantic similarity to
    word word based on the function similarity_fn.
    '''
    results = {}
    #First, get the results of the semantic similarity between
    #word and all of the options in choices
    for choice in choices:
        results[choice] = cosine_similarity(semantic_descriptors.get(word), semantic_descriptors.get(choice))

    #Now that we have a dictionary of the results of semantic similarity, we must determine
    #which word had the highest semantic similarity.
    highest_value = 0
    highest_key = 0
    for key, value in results.items():
        if value > highest_value:
            highest_value = value
            highest_key = key

    #Return the word with the highest semantic similarity
    return highest_key

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass

if __name__ == "__main__":
    filenames = ["text1.txt","text2.txt","text3.txt"]
    sol = build_semantic_descriptors_from_files(filenames)