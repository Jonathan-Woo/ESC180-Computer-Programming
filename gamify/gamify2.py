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
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = -1000

    star_anchor_1, star_anchor_2 = None, None
    
def star_can_be_taken(activity):
    '''Returns true iff a star can be used to get more hedons for
    activity activity. A star can only be taken if the user uses the star
    immediately after receiving it. Also, the user must not bored with 
    stars and the star was offered for activity activity. 
    '''
    pass

    
def perform_activity(activity, duration):
    '''Simulates the activity activity for duration minutes. Parameter
    duration is a positive int. If activity is not one of "running",
    "textbooks", or "resting", running the function should have no
    effect.
    '''
    pass

def get_cur_hedons():
    '''Returns the number of hedons that the user has accumulated so far.
    '''
    pass
    
def get_cur_health():
    '''Returns the number of health points that the user has accumulated
    so far.
    '''
    pass
    
def offer_star(activity):
    '''Offers a star to the user for any particular activity activity.
    Parameter activity is any of the three strings: "running",
    "textbooks", "resting"
    '''
    global star_anchor_1, star_anchor_2, cur_star
    
    
    #shortcut to leaving offer_star() if the user has already used 3
    #stars within a span of 2 hours
    if cur_star == 3:
        return None
        
    #removes tracking of old stars (those that are more than 120 minutes
    #old. 
    if cur_time - star_anchor_2 > 120:
        star_anchor_1, star_anchor_2 = 0, 0
        cur_star = 0
    elif cur_time - star_anchor_1 > 120:
        star_anchor_1 = star_anchor_2
        star_anchor_2 = 0
        cur_star = 1
    
    #sets tracking for new stars. If this is the third star within the
    #span of 2 hours, it switches star_invalid to true and prevents
    #the user from using stars for the rest of the simulation.
    if star_anchor_1 == 0:
        star_anchor_1 = cur_time
        cur_star = 1
        cur_star_activity = activity
    else:
        if star_anchor_2 == 0:
            star_anchor_2 = cur_time
            cur_star = 2
            cur_star_activity = activity
        else:
            cur_star = 3
        
def most_fun_activity_minute():
    '''Returns the activity ("running", "textbooks", or "resting") which 
    would give the most hedons if the person performed it for one minute 
    at the current time.
    '''
    pass
    
################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
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
    
    
