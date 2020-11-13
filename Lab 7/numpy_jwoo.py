'''
#Needed for array() and dot()
from numpy import *


#Printing matrices using NumPy:

#Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = array(M_listoflists)
#Now print it:
print(M)




#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = array([[1,-2,3],[3,10,1],[1,5,3]])
x = array([75,10,-11])
b = dot(M,x)

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

#To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist()

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]
'''
###########################################################

#Problem 1
def print_matrix(M_lol):
    '''Prints list of list interpretation of matrix M_lol
    '''
    print(M_lol.tolist())

#Problem 2
def get_lead_ind(row):
    '''Finds the first index of the first non-zero element in row
    '''
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

#Problem 3
def get_row_to_swap(M, start_i):
    '''Returns the row that needs to be swapped.
    That row is the one with leading non-zero furthest to the left
    '''
    smallest_index = inf
    row_number = inf
    for row in range(start_i, len(M)):
        if get_lead_ind(M[row]) < smallest_index:
            smallest_index = get_lead_ind(M[row])
            row_number = row
    return row_number + 1

#Problem 4
def add_rows_coefs(r1, c1, r2, c2):
    '''Multiplies coefficients c1 and c2 by rows r1 and r2 respsectively.
    Returns their sum.
    '''
    result = [0] * len(r1)
    for i in range(len(result)):
        result[i] = c1 * r1[i] + c2 * r2[i]
    return result

#Problem 5
def eliminate(M, row_to_sub, best_lead_ind):
    '''Eliminates rows below row_to_sub by finding a coefficient applied to
    best_lead_ind of row_to_sub such that all rows below row_to_sub at
    best_lead_ind become 0.
    '''
    coefficient = None
    subtraction_value = M[row_to_sub][best_lead_ind]
    for row in range(row_to_sub + 1, len(M)):
        coefficient = M[row][best_lead_ind]/subtraction_value
        for col in range(best_lead_ind,len(M[0])):
            M[row][col] = M[row][col] - (subtraction_value * coefficient)

#Problem 6
def forward_step(M):
    '''Applies the forward step of Gaussian elimination.
    Starts with rearranging rows so that rows are arranged in order of
    decreasing leading non-zero index.
    '''
    for count in range(len(M)):
        M[count], M[get_row_to_swap(M, count)] = M[get_row_to_swap(M, count)], M[count]
        print("Rearrange", str(count + 1))
        print(M)
        eliminate(M, count, get_lead_ind(M[count]))
        print("Eliminate", str(count + 1))
        print(M)

if __name__ == '__main__':
    M = [[0,0,1,0,2],[1,0,2,3,4],[3,0,4,2,1],[1,0,1,1,2]]



