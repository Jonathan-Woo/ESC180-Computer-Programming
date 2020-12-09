
# Problem 1

def power(x, n):
    ''' Returns x^n'''
    if n == 0:
        return 1
    
    return x * power(x, n - 1)

# Problem 2

def interleave(L1, L2):
    ''' Returns a list with L1 and L2 interleaved'''
    # [L1[0], L2[0], L1[1], L2[1], ..., L1[n-1], L2[n-1]] (here, n == len(L1) == len(L2)
    ans = []
    n = len(L1)
    
    if n == 1:
        ans.append(L1[0])
        ans.append(L2[0])
        return ans
    
    ans.append(L1[n - 1])
    ans.append(L2[n - 1])
    
    return (interleave(L1[:n - 1], L2[:n - 1])) + ans

# Problem 3

def reverse_loop(L):
    ''' Reverses a list'''
    
    # L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # L[-1-i] = 9, 8, 7, 6
    
    # for i in range(len(L)//2):
        # L[i], L[-1-i] = L[-1-i], L[i]
    
    length = len(L)
    mid = len(L) // 2
    ans = []
    
    if length == 1:
        ans.append(L[0])
        return ans
    
    L[length - 1], L[-1-(length - 1)] = L[-1-(length - 1)], L[length - 1]
    
    return reverse_loop(L[:mid-1]) + ans
        
        
# Problem 4

def zigzag1(L):
    '''Prints a list L in the order: L[n//2] L[n//2-1] L[n//2+1] 
    L[n//2-2]...
    
    Works for both even and odd lists.
    '''
    #base case
    if len(L) == 0:
        print('')
    elif len(L) == 1:
        print(L[0], end = "")
        
    #even case
    elif len(L) % 2 != 0:
        print(L[len(L)//2])
        zigzag1(L[0:len(L)//2] + L[len(L)//2 + 1:])
    #odd case
    else:
        print(L[len(L)//2], L[len(L)//2 - 1], end = "\n")
        zigzag1(L[0:len(L)//2 - 1] + L[len(L)//2+1:])
                
# Problem 5
def is_balanced(s):
    ''' Returns True iff the string s has balanced ()
    '''
    #The idea is to assume that an open bracket will match with the
    #first close bracket and a close bracket will match with the
    #nearest open bracket.
    
    loc_start = 0
    loc_end = 0
    if '(' in s and ')' in s:
        loc_start = s.index('(')
        loc_end = s.index(')')
        if loc_start < loc_end:
            s = s[loc_start + 1:loc_end] 
            return is_balanced(s)
        else:
            return False
    
    #base cases
    #if only one bracket exists in s, then there is no other 
    #bracket to match it with and it must not be balanced
    elif '(' in s or ')' in s:
        return False
    
    #if you've reached an s with no brackets, the original s is
    #balanced
    else:
        return True