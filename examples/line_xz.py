from bricklayer.levels.level_2 import line_xz, BLACK_BRICK, output, inc_offset_2D, smooth_line_xz

line_xz((0, 0), (3, 10), BLACK_BRICK)
inc_offset_2D(3, 3)
smooth_line_xz((0, 0), (3, 10), BLACK_BRICK)
output()
