from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    user_name = []
    d = data['messages']
    for i in d:
        user_name =user_name + [i.get('actor','yoq')]
    z = set(user_name)
    z = list(z)
    x = z.pop(z.index('yoq'))
    return z
data = read_data('data/result.json')
print(find_all_users_name(data))