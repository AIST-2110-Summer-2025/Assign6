

def format_float(num: float, max_decimals: int = None) -> str:
    '''
    This function takes any floating point number and returns a string
    representation that has AT MOST a specified number of digits after the
    decimal point. All trailing 0's are removed. If no digits remain after the
    decimal point, then the decimal point is removed.

    In other words, this displays numbers like rational human beings expect them
    to be displayed.
    
    Parameters
    ----------
    num : float
        The number to format.
    max_decimals : int 
        Optional. The maximum number of digits following the decimal. If not
        specified, the number will not be rounded, but will still have all
        trailing zeroes removed.

    Returns
    -------
    str
        The float formatted as a string for normal humans.
    '''
    
    if max_decimals is not None:
        if type(max_decimals) is int and max_decimals >= 0:
            num = round(num, max_decimals)
        else:
            raise ValueError(f"{max_decimals} must be an int greater than or equal to 0")
    num_str = str(num)
    if 'e' in num_str:
        return num_str
    while num_str[-1] == '0':
        num_str = num_str[:-1]
    if num_str[-1] == '.':
        num_str = num_str[:-1]
    return num_str
