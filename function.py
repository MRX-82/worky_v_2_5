"""
This is small function for working aplication "worky"
"""

def integer_to_string(counter, number):
    """
    This function do it translate integer to string for watch to display
    """
    counter = str(counter)
    testing_counter = len(counter)
    if testing_counter < number:
        nead_number = number - testing_counter
        new_counter = '0'*nead_number+counter
        return new_counter
    elif testing_counter == number:
        new_counter = counter
        return new_counter

def string_to_integer(counter):
    """
    This function do it translate string to integer for work aplication "worky"
    """
    new_counter = int(counter)
    return new_counter

def repack_download_counter(pack_counter):
    """
    This is function for repacking download unit
    """
    try:
        Login, counter_odo, counter_dst = pack_counter[0][1], pack_counter[0][2], pack_counter[0][3]
        return Login, counter_odo, counter_dst
    except IndexError: #Если основная запись в бд повредиться
        return 'None', 0, 0

def big_number(counter, n):
    if counter == n:
        counter = 0
        return counter
    else:
        return counter

def reserv_load_save(Login):
    n = len(Login)
    Login = Login[0:n-1]
    return Login

