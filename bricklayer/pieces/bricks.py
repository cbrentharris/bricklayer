from bricklayer.pieces.enums import Color, Shape
import uuid

class Brick:
    u"""
    LDD XML bricks are composed of a shape and a color
    """

    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
        self.identifier = uuid.uuid4().int

# Grayscale bricks
BLACK_BRICK            = Brick(Color.BLACK, Shape.BIT)
TITANIUM_BRICK         = Brick(Color.TITANIUM, Shape.BIT)
GRAY_BRICK             = Brick(Color.GRAY, Shape.BIT)
STONE_GRAY_BRICK       = Brick(Color.STONE_GRAY, Shape.BIT)
LIGHT_GRAY_BRICK       = Brick(Color.LIGHT_GRAY, Shape.BIT)
SILVER_BRICK           = Brick(Color.SILVER, Shape.BIT)
WHITE_BRICK            = Brick(Color.WHITE, Shape.BIT)
WHITE_GLOW_BRICK       = Brick(Color.WHITE_GLOW, Shape.BIT)

DARK_GREEN_BRICK       = Brick(Color.DARK_GREEN, Shape.BIT)
GREEN_BRICK            = Brick(Color.GREEN, Shape.BIT)
OLIVE_BRICK            = Brick(Color.OLIVE, Shape.BIT)
BRIGHT_GREEN_BRICK     = Brick(Color.BRIGHT_GREEN, Shape.BIT)
LIGHT_GREEN_BRICK      = Brick(Color.LIGHT_GREEN, Shape.BIT)
ARMY_GREEN_BRICK       = Brick(Color.ARMY_GREEN, Shape.BIT)
SPRING_BRICK           = Brick(Color.SPRING, Shape.BIT)

INDIGO_BRICK           = Brick(Color.INDIGO, Shape.BIT)
BLUE_BRICK             = Brick(Color.BLUE, Shape.BIT)
LIGHT_ROYAL_BLUE_BRICK = Brick(Color.LIGHT_ROYAL_BLUE, Shape.BIT)
BLUE_BRICK             = Brick(Color.BLUE, Shape.BIT)
GRAY_BLUE_BRICK        = Brick(Color.GRAY_BLUE, Shape.BIT)
AQUA_BRICK             = Brick(Color.AQUA, Shape.BIT)
LIGHT_AQUA_BRICK       = Brick(Color.LIGHT_AQUA, Shape.BIT)

RED_BRICK              = Brick(Color.RED, Shape.BIT)
DARK_RED_BRICK         = Brick(Color.DARK_RED, Shape.BIT)
PINK_BRICK             = Brick(Color.PINK, Shape.BIT)
LIGHT_PINK_BRICK       = Brick(Color.LIGHT_PINK, Shape.BIT)

NOUGAT_BRICK           = Brick(Color.NOUGAT, Shape.BIT)
MEDIUM_NOUGAT_BRICK    = Brick(Color.MEDIUM_NOUGAT, Shape.BIT)
LIGHT_NOUGAT_BRICK     = Brick(Color.LIGHT_NOUGAT, Shape.BIT)

BROWN_BRICK            = Brick(Color.BROWN, Shape.BIT)
DARK_BROWN_BRICK       = Brick(Color.DARK_BROWN, Shape.BIT)
LIGHT_BROWN_BRICK      = Brick(Color.LIGHT_BROWN, Shape.BIT)

ORANGE_BRICK           = Brick(Color.ORANGE, Shape.BIT)

YELLOW_BRICK           = Brick(Color.YELLOW, Shape.BIT)
COOL_YELLOW_BRICK      = Brick(Color.COOL_YELLOW, Shape.BIT)
WARM_GOLD_BRICK        = Brick(Color.WARM_GOLD, Shape.BIT)
BRICK_YELLOW_BRICK     = Brick(Color.BRICK_YELLOW, Shape.BIT)

VIOLET_BRICK           = Brick(Color.VIOLET, Shape.BIT)
REDDISH_VIOLET_BRICK   = Brick(Color.REDDISH_VIOLET, Shape.BIT)
LAVENDER_BRICK         = Brick(Color.LAVENDER, Shape.BIT)
DARK_LAVENDER_BRICK    = Brick(Color.DARK_LAVENDER, Shape.BIT)

TRANSPARENT_BRICK      = Brick(Color.TRANSPARENT, Shape.BIT)

CLEAR_BRICK            = Brick(Color.CLEAR, Shape.BIT)
CLEAR_BLUE_BRICK       = Brick(Color.CLEAR_BLUE, Shape.BIT)
CLEAR_LIGHT_BLUE_BRICK = Brick(Color.CLEAR_LIGHT_BLUE, Shape.BIT)
CLEAR_RED_BRICK        = Brick(Color.CLEAR_RED, Shape.BIT)
CLEAR_PINK_BRICK       = Brick(Color.CLEAR_PINK, Shape.BIT)
CLEAR_VIOLET_BRICK     = Brick(Color.CLEAR_VIOLET, Shape.BIT)
CLEAR_GREEN_BRICK      = Brick(Color.CLEAR_GREEN, Shape.BIT)
CLEAR_YELLOW_BRICK     = Brick(Color.CLEAR_YELLOW, Shape.BIT)
CLEAR_ORANGE_BRICK     = Brick(Color.CLEAR_ORANGE, Shape.BIT)
CLEAR_BROWN_BRICK      = Brick(Color.CLEAR_BROWN, Shape.BIT)

BLACK_ROUND_BRICK      = Brick(Color.BLACK, Shape.ROUND)
GRAY_ROUND_BRICK       = Brick(Color.GRAY, Shape.ROUND)
LIGHT_GRAY_ROUND_BRICK = Brick(Color.LIGHT_GRAY, Shape.ROUND)
WHITE_ROUND_BRICK      = Brick(Color.WHITE, Shape.ROUND)

GREEN_ROUND_BRICK      = Brick(Color.GREEN, Shape.ROUND)
LIGHT_GREEN_ROUND_BRICK = Brick(Color.LIGHT_GREEN, Shape.ROUND)
ARMY_GREEN_ROUND_BRICK = Brick(Color.ARMY_GREEN, Shape.ROUND)

INDIGO_ROUND_BRICK = Brick(Color.INDIGO, Shape.ROUND)
BLUE_ROUND_BRICK = Brick(Color.BLUE, Shape.ROUND)
SKY_BLUE_ROUND_BRICK = Brick(Color.SKY_BLUE, Shape.ROUND)
LIGHT_BLUE_ROUND_BRICK = Brick(Color.LIGHT_BLUE, Shape.ROUND)
GRAY_BLUE_ROUND_BRICK = Brick(Color.GRAY_BLUE, Shape.ROUND)
AQUA_ROUND_BRICK = Brick(Color.AQUA, Shape.ROUND)

DARK_RED_ROUND_BRICK = Brick(Color.DARK_RED, Shape.ROUND)
RED_ROUND_BRICK = Brick(Color.RED, Shape.ROUND)
PINK_ROUND_BRICK = Brick(Color.PINK, Shape.ROUND)

DARK_BROWN_ROUND_BRICK = Brick(Color.DARK_BROWN, Shape.ROUND)
BROWN_ROUND_BRICK = Brick(Color.BROWN, Shape.ROUND)
LIGHT_BROWN_ROUND_BRICK = Brick(Color.LIGHT_BROWN, Shape.ROUND)


