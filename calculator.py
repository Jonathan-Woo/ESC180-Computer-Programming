#Problem 2: Displaying the Current Value
def display_current_value():
    '''prints the current value
    '''
    print(f'Current value: {current_value}')

#Problem 3: Addition/Problem 4: global
def add(to_add):
    '''takes the integer/float paramater and adds to the current value
    '''
    global current_value, undo_value
    undo_value = current_value
    current_value += to_add

def subtract(to_subtract):
    '''takes the integer/float parameter and subtracts from the current value
    '''
    global current_value, undo_value
    undo_value = current_value
    current_value -= to_subtract

#Problem 5: Multiplication and Division
def multiply(to_multiply):
    '''takes the integer/float paramter and multiplies with the current value
    '''
    global current_value, undo_value
    undo_value = current_value
    current_value *= to_multiply

def divide(to_divide):
    '''takes the integer/float paramater and divides with the current value
    '''
    global current_value
    undo_value = current_value
    current_value /= to_divide

#Problem 6: Memory and Recall (challenge)
def memory():
    '''stores a value in memory when called
    only stores one value, overwrites previous memory value
    '''
    global memory_value
    memory_value = current_value

def recall():
    '''updates the current value with the previously stored memory value
    '''
    return memory_value

#Problem 7: Undo (challenge)
def undo():
    '''updates the current value with the preceding value which is updated every time an operation occurs
    after undoing, the preceding (undo) value becomes the former current value
    '''
    global current_value,undo_value,undo_temp
    undo_temp = undo_value
    undo_value = current_value
    current_value = undo_temp

#Problem 1: Welcome Message
if __name__ == "__main__":
    current_value = 0.0
    memory_value = 0.0
    undo_value = 0.0
    undo_temp = 0.0

    display_current_value()
    add(5)
    subtract(2)
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    multiply(10)
    display_current_value()
    undo()
    undo()
    display_current_value()
    undo()
    undo()
    undo()
    display_current_value()






