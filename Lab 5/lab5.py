#Problem 1
def list1_start_with_list2(list1, list2):
    '''Takes 2 lists, returns true if list1 is at least as large as list2 and
    whether the items of list 2 are identical and in the same order as list1
    '''
    if len(list1) >= len(list2):
        for i in range (len(list2)):
            if list2[i] != list1[i]:
                return False
        return True
    return False

#Problem 2
def match_pattern(list1, list2):
    '''Checks if items in list2 are in list1 in the same order
    '''
    #Simple solution that breaks down all of the logic gates and loops
    for i in range(len(list1)):
        if list2[0] == list1[i]:
            for e in range(len(list2)):
                if list1[i + e] != list2[e]:
                    break
                if e == len(list2)-1:
                    return True
            break
    return False

    #Much more concise solution
    #Iterates through all elem in list2 are in list1
    #return(all(elem in list1 for elem in list2))

#Problem 3
def repeats(list0):
    '''Checks if list0 containts at least two adjacent elements with the same value
    '''
    for i in range (len(list0)-1):
        if list0[i] == list0[i + 1]:
            return True
    return False

#Problem 4a
def print_matrix_dim(M):
    '''Takes a list M and prints its dimensions
    '''
    print(str(len(M)) + "x" + str(len(M[0])))

#Problem 4b
def mult_M_v(M, v):
    '''Takes a matrix M and vector v
    Returns the dot product of M and v (Mv)
    '''
    product_vector = []
    append_value = 0
    for i in range (len(M)):
        for e in range (len(M[0])):
            append_value += M[i][e] * v[e]
        product_vector.append(append_value)
        append_value = 0
    return product_vector

#Problem 4c
def mult_M_N(M, N):
    '''Takes 2 matrices M and N
    Calculates the product of M x N
    '''
    product_matrix = []
    append_value = 0
    append_list = []
    for i in range (len(M)):
        for e in range (len(N[0])):
            for f in range(len(N)):
                append_value += M[i][f] * N[f][e]
            append_list.append(append_value)
            append_value = 0
        product_matrix.append(append_list)
        append_list = []
    return product_matrix

if __name__ == "__main__":
    print(mult_M_N([[1,2,3],[0,1,2]],[[1,2],[3,4],[5,6]]))