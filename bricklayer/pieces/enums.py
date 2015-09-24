class LDDXML:
    u"""
    names for XML in LDD values
    """
    COLOR_ID = "materialID"
    SHAPE_ID = "designID"

class Orientation:
    u"""
    An enum defining the orientation values for different orientations
    """
    LEFT = '0,0,-1,0,0.99999994039535522,0,1,0,0'
    RIGHT = '0,0,1,0,0.99999982118606567,0,-1,0,0'
    FRONT = '-1,0,0,0,0.99999988079071045,0,0,0,-1'
    BACK = '1,0,0,0,1,0,0,0,1'
    NORMAL = '1,0,0,0,1,0,0,0,1'

class Shape:
    u""" 
    An enum defining the shapes for shape constants in LDD
    """
    BIT = '3005'
    ROUND = '3062'
    NOSE_CONE = '4589'
    WEDGE = '50746'

class Dimensions:
    u"""
    In LDD, bricks have a specific width and height
    """
    BRICK_WIDTH = .8
    BRICK_HEIGHT = .96

class Color:
    u"""
    An enum defining the color constants in LDD
    """

    BLACK = "26"
    TITANIUM = "316"
    GRAY = "199"
    STONE_GRAY = "208"
    LIGHT_GRAY = "194"
    SILVER = "315"
    WHITE = "1"
    WHITE_GLOW = "329"

    DARK_GREEN = "141"
    GREEN = "28"
    BRIGHT_GREEN = "37"
    SPRING = "326"
    OLIVE = "330"
    LIGHT_GREEN = "119"
    ARMY_GREEN = "151"

    INDIGO = "140"
    BLUE = "23"
    SKY_BLUE = "321"
    LIGHT_BLUE = "102"
    LIGHT_ROYAL_BLUE = "212"
    GRAY_BLUE = "135"
    AQUA = "322"
    LIGHT_AQUA = "323"

    DARK_RED = "154"
    RED = "21"
    PINK = "221"
    LIGHT_PINK = "222"
    
    NOUGAT = "18"
    MEDIUM_NOUGAT = "312"
    LIGHT_NOUGAT = "283"

    VIOLET = "268"
    REDDISH_VIOLET = "124"
    LAVENDER = "325"
    DARK_LAVENDER = "324"

    DARK_BROWN = "192"
    BROWN = "38"
    LIGHT_BROWN = "5"

    ORANGE = "106"
    GOLD = "191"
    YELLOW = "24"
    COOL_YELLOW = "226"
    WARM_GOLD = "297"
    BRICK_YELLOW = "5"

    TRANSPARENT = "40"

    CLEAR = "143"
    CLEAR_RED = "41"
    CLEAR_LIGHT_BLUE = "42"
    CLEAR_BLUE = "43"
    CLEAR_GREEN = "48"
    CLEAR_PINK = "113"
    CLEAR_VIOLET = "126"
    CLEAR_YELLOW = "44"
    CLEAR_ORANGE = "182"
    CLEAR_BROWN = "111"


