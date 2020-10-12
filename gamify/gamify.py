#WHAT IS LAST FINISHED?

def initialize():
    '''Initializes the global variables needed for the simulation.
    '''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars

    global star_anchor_1, star_anchor_2
    
    global cur_star, cur_star_activity

    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = 10000000

    star_anchor_1, star_anchor_2 = -200, -200
    
def star_can_be_taken(activity):
    '''Returns true iff a star can be used to get more hedons for
    activity activity. A star can only be taken if the user uses the star
    immediately after receiving it. Also, the user must not bored with 
    stars and the star was offered for activity activity. 
    '''
    return cur_star_activity == activity

    
def perform_activity(activity, duration):
    '''Simulates the activity activity for duration minutes. Parameter
    duration is a positive int. If activity is not one of "running",
    "textbooks", or "resting", running the function should have no
    effect.
    '''
    global cur_health, cur_hedons, last_finished, cur_star_activity, cur_time, last_activity, last_activity_duration
    if num_error(duration):
        pass
    if str_activity_error(activity):
        pass

    #checks if previous activity was the same. If not, resets activity time.
    if not(last_activity == activity):
        last_activity_duration = 0

    #uses stars
    use_star(activity, duration)

    #running health
    if activity == "running":
        if (last_activity_duration + duration) <= 180:
            cur_health += 3 * duration
        else:
            if (180 - last_activity_duration) > 0:
                cur_health += ((180 - last_activity_duration) * 3) + (duration - (180 - last_activity_duration))
            else:
                cur_health += (duration)
            pass
        #running hedons
        if (is_tired() == True):
            cur_hedons -= 2 * duration
        elif duration <= 10:
            cur_hedons += 2 * duration
        else:
            cur_hedons += (10 * 2) - (2 * (duration - 10))
            
    #textbooks health
    if activity == "textbooks":
        cur_health += 2 * duration
        #textbooks hedons
        if (is_tired() == True):
            cur_hedons -= 2 * duration
        elif duration <= 20:
            cur_hedons += 2 * cur_hedons
        else:
            cur_hedons += 20 - (duration - 20)
    
    #resting
    if activity == "resting":
        last_finished += duration
        last_activity = activity
        cur_time += duration
        pass

    #Consecutive activities
    if last_activity == activity:
        last_finished = 0
        last_activity_duration += duration
        cur_time += duration
        pass

    last_activity_duration = duration
    last_activity = activity
    last_finished = 0   
    cur_time += duration
    cur_star_activity = None

def get_cur_hedons():
    '''Returns the number of hedons that the user has accumulated so far.
    '''
    return(cur_hedons)
    
def get_cur_health():
    '''Returns the number of health points that the user has accumulated
    so far.
    '''
    return(cur_health)
    
def offer_star(activity):
    '''Offers a star to the user for any particular activity activity.
    Parameter activity is any of the three strings: "running",
    "textbooks", "resting"
    '''
    global star_anchor_1, star_anchor_2, cur_star, bored_with_stars, cur_star_activity

    str_activity_error(activity)

    #shortcut to leaving offer_star() if the user has already used 3
    #stars within a span of 2 hours
    if bored_with_stars == True:
        pass
        
    #removes tracking of old stars (those that are more than 120 minutes
    #old. 
    if ((cur_time - star_anchor_2) > 120):
        star_anchor_1, star_anchor_2 = cur_time, cur_time
        cur_star = 0
    elif (((cur_time - star_anchor_1) <= 120) and cur_star == 1):
        star_anchor_2 = cur_time
    elif ((cur_time - star_anchor_1) > 120):
        star_anchor_1 = star_anchor_2
        star_anchor_2 = cur_time
        cur_star = 1
    else:
        bored_with_stars = True
        pass
    
    #sets tracking for new stars. If this is the third star within the
    #span of 2 hours, it sets bored_with_stars to True and prevents
    #the user from using stars for the rest of the simulation.
    if cur_star == 0:
        cur_star = 1
        cur_star_activity = activity
    else:
        if cur_star == 1:
            cur_star = 2
            cur_star_activity = activity

def use_star(activity, duration):
    global cur_hedons, cur_star_activity

    if cur_star_activity == activity:
        if duration <= 10:
            cur_hedons += duration * 3
        else:
            cur_hedons += 10 * 3
    cur_star_activity = None
        
def most_fun_activity_minute():
    '''Returns the activity ("running", "textbooks", or "resting") which 
    would give the most hedons if the person performed it for one minute 
    at the current time.
    '''
    running_hedons, textbook_hedons = 0, 0

    #running hedons
    if cur_star_activity == "running":
        running_hedons += 3

    if (is_tired() == True):
        running_hedons += -2
    else:
        running_hedons += 2
    
    #textbook hedons
    if cur_star_activity == "textbooks":
        textbook_hedons += 3

    if (is_tired() == True):
        textbook_hedons += -2
    else:
        textbook_hedons += 2

    highest_value = max(textbook_hedons, running_hedons, 0)
    dict = {
        textbook_hedons: "textbooks",
        running_hedons: "running",
        0: "resting"
    }
    return dict.get(highest_value)

#helper functions

def num_error(num):
    '''Checks if a number is valid or not.
    '''
    if num == 0 or num %1 != 0:
        print("Invalid number. Enter positive integer.")
        return True
    return False
        
def str_activity_error(activity):
    '''Checks if a string is one of running, textbooks, or resting.
    '''
    if not(activity in ["running", "textbooks", "resting"]):
        print("Invalid input. Enter one of: running, textbooks, or resting.")
        return True
    return False

def is_tired():
    '''Checks if the user is tired
    '''
    if (last_activity in ["running", "textbooks"] or last_finished < 120):
        return True
    return False

################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            #-20 = 10 * 2 + 20 * (-2)
    print(get_cur_health())            #90 = 30 * 3
    print(most_fun_activity_minute())  #resting
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  #running
    perform_activity("textbooks", 30)  
    print(get_cur_health())            #150 = 90 + 30*2
    print(get_cur_hedons())            #-80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            #210 = 150 + 20 * 3
    print(get_cur_hedons())            #-90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health())            #700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons())            #-430 = -90 + 170 * (-2)
    
