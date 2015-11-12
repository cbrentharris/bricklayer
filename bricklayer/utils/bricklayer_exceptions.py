"""

This package contains all custom exceptions being used by bricklayer to simplify messages comminicated
to new end user

"""

class OutOfBoundsException(Exception):
    u"""
    Used for when a user tries to add a brick to the virtual space, but its out of the virtual
    space bounds
    """
    pass
