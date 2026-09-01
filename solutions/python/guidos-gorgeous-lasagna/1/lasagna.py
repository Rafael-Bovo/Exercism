''' 
Parameters:
EXPECTED_BAKE_TIME (int): the time needed to cook a lasagna 
TIME_TO_MAKE_A_LAYER (int): the time needed to prepare a layer on a lasagna
'''

EXPECTED_BAKE_TIME = 40
TIME_TO_MAKE_A_LAYER = 2

def bake_time_remaining(preparation_time):
    '''
    Calculate the time remaing to cook the lasagna

    Parameters:
    preparation_time (int): represents how much time had already passed cooking 

    Returns:
    int: The total time remaining (in minutes) to cook the lasagna

    '''

    elapsed_bake_time = EXPECTED_BAKE_TIME - preparation_time

    return elapsed_bake_time

def preparation_time_in_minutes(number_of_layers) :
    '''
    Calculate the time needed to construct a lasagna with 'number_of_layers' number of layers

    Parameters:
    number_of_layers (int): The number of layers in the recipe

    Returns:
    int: The total number of time ( in minutes ) needed to prepare the layers

    '''
    
    time_to_make_the_layers = TIME_TO_MAKE_A_LAYER * number_of_layers

    return time_to_make_the_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''
    Calculate the total time needed to prepare the recipe

    Parameters:
    number_of_layers (int): The number of layers in the recipe
    elapsed_bake_time (int): The total number of time ( in minutes ) needed to prepare the layers

    Returns:
    int: The total time to prepare the recipe
    '''

    elapsed_time_recipe = elapsed_bake_time + (number_of_layers*TIME_TO_MAKE_A_LAYER)

    return elapsed_time_recipe
    
