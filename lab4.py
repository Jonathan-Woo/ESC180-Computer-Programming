def sum_nums(L):
    s = 0
    for num in L:
        s += num
    return s


# Problem 1 (done)

def count_evens(L):
    ''' Returns the number of even integers in the list L[int]
    '''
    counter = 0
    for i in range(len(L)):
        if L[i] % 2 == 0:
            counter += 1

    return counter

# Problem 2 (need to figure out how to structure str_lis)
# lis = [0, 1], returns '[0, 1, ]'

def list_to_str(lis):
    ''' Returns the string representation of the list lis[int]
    '''
    str_lis = ""
    for i in range(len(lis)):
        str_lis += str(lis[i]) + ", "
    return("[" + str_lis + "]")


# Problem 3 (done)

def lists_are_the_same(list1, list2):
    ''' Returns True iff list1 and list2 contain the same elements
    in the same order
    '''
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                return True
            else:
                return False
    else:
        return False

# Problem 4 (done)

def simplify_fraction(n, m):
    ''' Returns simplified version of the fraction n/m
    '''
    gdc = euclid(n, m)
    print(n // gdc , "/" , m // gdc)


# Problem 5

def lebiniz_formula(n):
    '''Calculates and returns the lebiniz formula from
    0 to n
    '''
    lebiniz_total = 0
    for i in range (0, n + 1):
        lebiniz_total += ((-1) ** i) / (2 * i + 1)
    return lebiniz_total * 4

def pi_approx():
    ''' Returns the number of terms required to obtain an approximation
    of pi to n sig digs
    '''
    # 1000000 gives 3.1415936535887745 (17 sig digs)

# Problem 6 (done)

def euclid(a, b):
    if a == 0:
        return b

    return euclid(b % a, a)