import calculator

def sum_of_cubes(n):
    '''Calculates and returns the sum of cubes from 1 to
    n. Uses a for loop to iteratively add the next value to
    the existing total.
    '''
    global total
    total = 0

    if n <= 0 or n % 1 != 0:
        print("Value invalid. Cannot find sum of cubes. Choose an integer >= 1.")
        return None

    for i in range (1, n + 1):
        total += (i**3)
    return total

def sum_of_cubes_formula(n):
    '''Calculates and returns the sum of cubes from 1 to n.
    Uses a formula.
    '''
    if n <= 0 or n % 1 != 0:
        print("Value invalid. Cannot find sum of cubes. Choose an integer >= 1.")
        return None

    return (n * (n + 1) / 2) ** 2

def check_sum(n):
    '''Calls on both sum_of_cubes() and
    sum_of_cubes_formula() to see if their sums are equal.
    If they are, this returns True, otherwise, it returns
    False.
    '''
    if n <= 0 or n % 1 != 0:
        print("Value invalid. Choose an integer >= 1.")
        return None

    return (sum_of_cubes(n) == sum_of_cubes_formula(n))

def check_sums_up_to_n(n):
    '''Checks if the sum of cubes from sum_of_cubes() and
    sum_of_cubes_formula() are equal for all values 1
    to n.
    '''
    if n <= 0 or n % 1 != 0:
        print("Value invalid. Choose an integer >= 1.")
        return None

    for i in range(1, n + 1):
        if not check_sum(i):
            return False
    return True

#Problem 3: Pi
def lebiniz_formula(n):
    '''Calculates and returns the lebiniz formula from
    0 to n
    '''
    if n <= 0 or n % 1 != 0:
        print("Value invalid. Cannot calculate pi. Choose an integer >= 1.")
        return None

    lebiniz_total = 0
    for i in range (0, n + 1):
        lebiniz_total += ((-1) ** i) / (2 * i + 1)
    return lebiniz_total * 4

if __name__ == '__main__':

    #Problem 1: Test calculator.py
    calculator.initialize()
    calculator.add(42)
    calculator.display_current_value()
    if calculator.get_current_value() == 42:
        print("Test 1 passed")
    else:
        print("Test 1 failed")


    #Test functions.


