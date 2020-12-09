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
    #If either vec1 or vec2 do not have any semantic descriptors, they cannot be
    #compared. Their default cosine_similarity is then 0.
    if len(vec1) == 0 or len(vec2) == 0:
        return -1

    #Firstly, we need to find matching keys between vec1 and vec2
    matching = (set(vec1.keys()).intersection(set(vec2.keys())))

    #Solve for the numerator of the equation
    numerator = 0
    for i in matching:
        numerator += (vec1.get(i) * vec2.get(i))

    #Solve for the denominator of the equation
    denominator = norm(vec1) * norm(vec2)

    #Solve for cosine similarity
    return (numerator/denominator)

def build_semantic_descriptors(sentences):
    '''Returns a dictionary whose keys are words in the list
    sentences and values are the semantic descriptor of the words
    '''
    semantic_descriptors = {}
    #Since we know that duplicate words do not change the association.
    #In other words, the same words appearing more than once in a sentence
    #does not change the semantic similarity, we can make a set of the
    #words.
    for sublist in sentences:
        words = list(set(sublist))
        words = remove_empties(words)
        #Now, we have the individual words as a list without duplicates
        for word in words:
            word = word.lower()

            #For words that do not yet have an entry in semantic_descriptors
            #we must initialize an empty dictionary as their value since
            #we cannot add values to a dictionary that does not exist!
            if word not in semantic_descriptors:
                semantic_descriptors[word] = {}

            #here, we go through the same sentence but only add to
            #semantic_descriptors if the other words are not the words
            #under analysis. You cannot be associated with yourself!
            for other_words in sublist:
                other_words = other_words.lower()
                if word != other_words:
                    if other_words in semantic_descriptors[word]:
                        semantic_descriptors[word][other_words] += 1
                    #in this case, the value for the dictionary for
                    #key = word has no value yet. Although we have a key
                    #as other_words, the value is still None type. We must
                    #initialize it to an integer before adding in future
                    #cases. Since this case only runs for the first time
                    #other_words exists for the key word, then it must be
                    #equal to 1.
                    else:
                        semantic_descriptors[word][other_words] = 1
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
        text = open(filenames[filename], "r", encoding="latin-1").read()
        text = text.replace("\n", "")
        #Convert all punctuation types to "." so that we only have to
        #split once
        text = text.replace("!", ".").replace("?", ".")
        sentences = text.split(".")
        sentences = remove_empties(sentences)
        for item in sentences:
            #We convert all punctuation to spaces so that we only have to
            #split once.
            item = item.replace(",", " ").replace("-", " ").replace(":", " ").replace(";", " ").replace("*", " ").replace("$", " ").replace("%", " ").replace("@", " ").replace("&", " ").replace("#", " ")
            separated_sentences.append(remove_empties(item.split(" ")))

    return build_semantic_descriptors(separated_sentences)

def remove_empties(list):
    '''Helper function that removes the empty elements of a list list
    '''
    for item in list:
        if item == '':
            list.remove('')
        elif item == ' ':
            list.remove(' ')
    return list

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''Determines the word in the list choices that has the closest semantic similarity to
    word word based on the function similarity_fn.
    '''
    results = {}
    #First, get the results of the semantic similarity between
    #word and all of the options in choices
    for choice in choices:
        results[choice] = similarity_fn(semantic_descriptors.get(word, {}), semantic_descriptors.get(choice, {}))

    #Now that we have a dictionary of the results of semantic similarity, we must determine
    #which word had the highest semantic similarity.
    highest_value = -1
    highest_key = -1
    for key, value in results.items():
        if value > highest_value:
            highest_value = value
            highest_key = key

    if highest_key == -1:
        highest_key = choices[0]
    #Return the word with the highest semantic similarity
    return highest_key

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    '''Returns the percentage of questions on which most_similar_word()
    guesses the right word where the right word is given.
    '''
    #Firstly, we must convert the text file into a list of lists where
    #each list item is a sentence and sublists are the words of the
    #sentence.
    lines = open(filename, "r", encoding="latin1").read().split("\n")
    lines = remove_empties(lines)

    #Now we will evaluate most_similar_word()
    num_correct = 0
    words = []
    for line in lines:
        words = line.split(" ")
        sol = most_similar_word(words[0], words[2:], semantic_descriptors, similarity_fn)

        if sol == words[1]:
            num_correct += 1

    return (num_correct/len(lines))*100

if __name__ == "__main__":
    build_semantic_descriptors_from_files(["text1.txt"])
