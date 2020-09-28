#DO WE BE CONCISE OR DO WE BE CLEAR?

#write a docstring for every function
#put a blank line after every docstring comment
#each line must be less than 80 characters
'''Describe precisely what the function does.
• Do not reveal how the function does it.
• Make the purpose of every parameter clear.
• Refer to every parameter by name.
• Be clear about whether the function returns a value, and if so, what.
• Explain any conditions that the function assumes are true. Examples: “n is an int”, “n != 0”,
“the height and width of p are both even”.
• Be concise.
• Ensure that the text you write is grammatically correct.
• Write the docstring as a command (e.g., “Return the first . . . ”) rather than a statement (e.g.,
“Returns the first . . . ”).
'''

def initialize():
    '''initialize() initializes global variables and sets values for them.
    This is called at the beginning of the game.
    Has return value.
    '''
    #make sure to describe global variables (what kind of information the variable stores and properties)

    #health_points keeps track of the health points of a user/player.
    #health_points is initialized as/to 0 and remains an integer throughout.

    #hedons keeps track of the number of hedons a user/player has.
    #hedons is initiazlied as/to 0 and remains an integer throughout.
    global health_points, hedons, rest_time, star_cooldown_time
    health_points, hedons, rest_time, star_cooldown_time = 0, 0, 0, 0

def running(minutes):
    '''running() increased a users health points by 3 for up to 180 minutes
    and 1 health point per minute for every minute over 180 minutes.
    Takes a parameter (minutes) which is used to calculate the change in
    health_points and hedons.
    '''
    global health_points, hedons, rest_time

    #health points adjustment
    if minutes <= 180:
        health_points += minutes * 3
    else:
        health_points += 180 * 3 + (minutes - 180)

    #hedons adjustment
    #Checks if the user has rested for at least 2 hours before
    #the start of running. If they have, they gain 2 hedons for every
    #minute that has passed up to 10 minutes. After that, they lose 2
    #hedons per minute.
    if rest_time < 120:
        hedons -= minutes * 2
    else:
        if minutes <= 10:
            hedons += minutes * 2
        else:
            hedons += 10 * 2 - (minutes - 10) * 2

def resting():

def carrying_textbooks(minutes):
    global health_points, hedons, rest_time

    health_points += minutes * 2

    #hedons adjustment
    #Checks if the user has rested for at least 2 hours before
    #the start of running. If they have, they gain 2 hedons for every
    #minute that has passed up to 10 minutes. After that, they lose 2
    #hedons per minute.
    if rest_time < 120:
        hedons -= minutes * 2
    else:
        if minutes <= 20:
            hedons += minutes
        else:
            hedons += 20 - (minutes - 10)

def offer_star():


if __name__ == "__main__":