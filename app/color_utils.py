import re

class ColorUtils:
  REGEX = "^([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})$"

  def hex_to_matrix(hex_color: str):
    if (not ColorUtils.is_valid_hex(hex_color)):
      hex_color = "FFFFFF"

    if (len(hex_color) == 3):
      hex_color = hex_color[0] * 2 + hex_color[1] * 2 + hex_color[2] * 2

    matrix = [0] * 20
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255

    matrix[0] = int(r) if r == 1.0 or r == 0.0 else r
    matrix[6] = int(g) if g == 1.0 or g == 0.0 else g
    matrix[12] = int(b) if b == 1.0 or b == 0.0 else b
    matrix[18] = 1

    return matrix
  
  def is_valid_hex(color: str) -> bool:
    return bool(re.match(ColorUtils.REGEX, color))

  def decode(color: str):
    if (len(color) == 3):
      color = color[0] * 2 + color[1] * 2 + color[2] * 2

    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))