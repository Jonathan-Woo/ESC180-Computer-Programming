from numpy import *

# Problem 1
def print_matrix(M_lol):
    ''' Returns the nested list M_lol as a matrix
    '''
    print(array(M_lol))

# Problem 2
def get_lead_ind(row):
    ''' Returns the index of the first non-zero element of row
    '''
    # check every elem in list row
    for i in range(len(row)):
        # once came across a non-zero elem, return the idx of that elem
        if row[i] != 0:
            return i
    return len(row)

# Problem 3
def get_row_to_swap(M, start_i):
    ''' returns the row that needs to be swapped with the row M[start_i]
    '''
    # M = [[5, 6, 7, 8],
    #      [0, 0, 0, 1],
    #      [0, 0, 5, 2],
    #      [0, 1, 0, 0]]

    # start_i = 1,
    # [0, 0, 0, 1] needs to be swapped with [0, 1, 0, 0], so the function should return 3.

    # get the index of the first non-zero elem of M[start_i], store it into idx
    idx = get_lead_ind(M[start_i])

    # check the rest of the rows in matrix M, from start_i to the end
    list = []
    row_to_swap = start_i

    for row_num in range(start_i, len(M)):
        if get_lead_ind(M[row_num]) < idx:
            idx = get_lead_ind(M[row_num])
            row_to_swap = row_num
    return row_to_swap

# Problem 4
def add_rows_coefs(r1, c1, r2, c2):
    ''' takes rows r1, r2 and floats c1, c2,
    returns a new list that contains the row c1*r1 + c2r2
    '''
    list = []

    for i in range(len(r1)):
        list.append(r1[i]*c1 + r2[i]*c2)

    return list

# Problem 5
def eliminate(M, row_to_sub, best_lead_ind):
    # M = [[5, 6, 7, 8],
    #      [0, 0, 1, 1],
    #      [0, 0, 5, 2],
    #      [0, 0, 7, 0]]
    # row_to_sub = 1
    # need to operate M[2] and M[3]
    # best_lead_ind = 2

    # b / a is the value to multiply with a
    # in this case, b = M[i][best_lead_ind], a = M[row_to_sub][best_lead_ind]

    multipier = 0
    for i in range(row_to_sub + 1, len(M)):
        multiplier = -(M[i][best_lead_ind])/(M[row_to_sub][best_lead_ind])
        new_rows = add_rows_coefs(M[row_to_sub], multiplier, M[i], 1)
        M[i] = new_rows
    return M



# Problem 6
def forward_step(M):
    ''' applies the fwd step of GE to M'''
    print("Now performing the forward step")
    for i in range(len(M)):
        print("The matrix is currently:")
        print_matrix(M)
        print("Now looking at row", i)
        print("Swapping rows", i , "and" , get_row_to_swap(M, i), "so that entry",  get_lead_ind(M[get_row_to_swap(M, i)]), "in the current row is non-zero")

        # swap
        row_swap = get_row_to_swap(M, i)
        M[i], M[row_swap] = M[row_swap], M[i]
        print("The matrix is currently:")
        print_matrix(M)

        # elimination
        eliminate(M, i, get_lead_ind(M[i]))
        print("Adding row", i, "to rows below it to eliminate coefficients in column", get_lead_ind(M[i]))
        print("The matrix is currently:")
        print_matrix(M)
        print("=========================================================================")

def divide(row, coef):
    list = []

    for i in range(len(row)):
        list.append(row[i]*coef)

    return list




# Problem 7
def backward_step(M):
    ''' applies the bwd step of GE to M'''
    print("Now performing the backward step")
    for i in range(len(M)):
        print("Adding row", len(M)-(i+1), "to rows above it to eliminate coefficients in column", get_lead_ind(M[len(M)-(i+1)]))
        eliminate(M, len(M)-(i+1), get_lead_ind(M[len(M)-(i+1)]))
        print("The matrix is currently:")
        print_matrix(M)
        print("=========================================================================")

    print("Now dividing each row by the leading coefficient")
    for i in range(len(M)):
        M[i] = divide(M[i], M[i][get_lead_ind(M[i])])

    print("The matrix is currently:")
    print_matrix(M)























