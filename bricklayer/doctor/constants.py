from bricklayer.utils.colors import Colors

u"""
    The following constants will be used in collecting metrics.
"""
LEVEL_1_PREDEFINED_FUNCTIONS = [
    "put_2D_1x1_RED",
    "put_2D_1x1_WHITE",
    "put_2D_1x1_BLUE",
    "put_2D_1x1_YELLOW",
    "put_2D_1x1_GREEN",
    "put_2D_1x1_GRAY",
    "put_2D_1x1_BLACK",
    "put_2D_1x1_EMPTY",

    "put_2D_2x1_RED",
    "put_2D_2x1_WHITE",
    "put_2D_2x1_BLUE",
    "put_2D_2x1_YELLOW",
    "put_2D_2x1_GREEN",
    "put_2D_2x1_GRAY",
    "put_2D_2x1_BLACK",
    "put_2D_2x1_EMPTY",

    "put_2D_1x2_RED",
    "put_2D_1x2_WHITE",
    "put_2D_1x2_BLUE",
    "put_2D_1x2_YELLOW",
    "put_2D_1x2_GREEN",
    "put_2D_1x2_GRAY",
    "put_2D_1x2_BLACK",
    "put_2D_1x2_EMPTY",

    "put_2D_2x2_RED",
    "put_2D_2x2_WHITE",
    "put_2D_2x2_BLUE",
    "put_2D_2x2_YELLOW",
    "put_2D_2x2_GREEN",
    "put_2D_2x2_GRAY",
    "put_2D_2x2_BLACK",
    "put_2D_2x2_EMPTY",

    "put_2D_2x3_RED",
    "put_2D_2x3_WHITE",
    "put_2D_2x3_BLUE",
    "put_2D_2x3_YELLOW",
    "put_2D_2x3_GREEN",
    "put_2D_2x3_GRAY",
    "put_2D_2x3_BLACK",
    "put_2D_2x3_EMPTY",

    "put_2D_3x2_RED",
    "put_2D_3x2_WHITE",
    "put_2D_3x2_BLUE",
    "put_2D_3x2_YELLOW",
    "put_2D_3x2_GREEN",
]

class HelpMessages(object):
    BAD_INDENTATION = """
    {warning}Oops!{end_color} it appears that there was an indentation error. Spacing is {warning}**very**{end_color} important in python.
    Please look at your code carefully to make sure all the spacing is correct.
    It can also help to have a second set of eyes look over the code as well. 
    
    The line number referenced in the code will be very helpful in letting you know where the 
    problem is. For example, look at the following code:

    >>> animals = ['cat', 'dog']
    >>> for animal in animals:
    ... print animal
      File "<stdin>", line 2
          print animal
              ^
   IndentationError: expected an indented block

   Above, the code attempts to loop over the animals list and print the animal, but as you can see
   the "print animal" statement is not indented properly to be within the for loop block, and the 
   error happens. To correct, the working code looks more like

   >>> for animal in animals:
   ...{warning}     {end_color}print animal
   ...
   cat
   dog
    """.format(warning=Colors.Background.WARNING, end_color=Colors.ENDC)

    INCORRECT_FUNCTION_NAME = """
    Oops! It appears that you tried to use a function that is not available - {}. 
    Did you mean to try one of these:\n{} 
    """
