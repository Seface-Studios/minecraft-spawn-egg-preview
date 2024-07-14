import io
import uuid
import numpy as np
from PIL import Image

from app.color_utils import ColorUtils

PREVIEW_SIZE = (128, 128)
SPAWN_EGG_BASE_PATH = 'static/images/spawn_egg_base.png'
SPAWN_EGG_OVERLAYE_PATH = 'static/images/spawn_egg_overlay.png'

class SpawnEgg:
  def __init__(self, base_color: str, overlay_color: str) -> None:
    self.base_color = base_color
    self.overlay_color = overlay_color

  def get_mounted_spawn_egg_buffer(self):
    base_buffer = self.get_modified_buffer_from(SPAWN_EGG_BASE_PATH, self.base_color)
    overlay_buffer = self.get_modified_buffer_from(SPAWN_EGG_OVERLAYE_PATH, self.overlay_color)

    return self.merge_buffers(base_buffer, overlay_buffer)

  def get_modified_buffer_from(self, path: str, color: str):
    with Image.open(path) as img:
      img = img.resize(PREVIEW_SIZE, Image.NEAREST)
      matrix = ColorUtils.hex_to_matrix(color)

      print(color, matrix)

      img = img.convert("RGBA")
      img_data = np.array(img)
      transformed_data = img_data @ np.array(matrix).reshape(4, 5)[:, :4].T

      transformed_img = Image.fromarray(transformed_data.astype(np.uint8), 'RGBA')

      buffer = io.BytesIO()
      transformed_img.save(buffer, format = "PNG")
      buffer.seek(0)

      return buffer

  def merge_buffers(self, *buffers):
    merged_image: Image.Image = None

    for i, buffer in enumerate(buffers):
      to_merge_image = Image.open(buffer)

      if (i == 0):
        merged_image = to_merge_image
        continue

      position = (
        (merged_image.width - to_merge_image.width) // 2,
        (merged_image.height - to_merge_image.height) // 2
      )

      merged_image.paste(to_merge_image, position, to_merge_image)

    merged_buffer = io.BytesIO()
    merged_image.save(merged_buffer, format = "PNG")
    merged_buffer.seek(0)  

    return merged_buffer

  def get_uuid(self):
    return uuid.uuid5(uuid.NAMESPACE_DNS, f'{self.base_color}-{self.overlay_color}')