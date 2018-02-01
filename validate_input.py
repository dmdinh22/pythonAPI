import numbers

def is_valid(my_dict):
    """
    Check to see if the input dictionary is a correct input
    :param my_dict: input dictionary
    :return: boolean, True if valid, False if invalid
    """
    input_fields = ["x", "y"]

    # Iterate through fields e.g. 'x', and 'y'
    for field in input_fields:

        # Make sure we have the correct input fields by iterating though all fields we want to check
        if field not in my_dict.keys():
            return False

        # Make sure the values in the field are numbers
        if not isinstance(my_dict[field], numbers.Number):
            return False

    return True