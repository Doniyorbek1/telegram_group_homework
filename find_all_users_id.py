from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    user_id = []
    for i in data['messages']:
        user_id = user_id + [i.get('actor_id','yoq')]
    z = set(user_id)
    z = list(z)
    ls = z.pop(user_id.index('yoq'))
    return z

data = read_data('data/result.json')
print(find_all_users_id(data))
