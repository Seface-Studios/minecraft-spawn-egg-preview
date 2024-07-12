import io
import base64
from PIL import Image
from flask import Flask, send_file, make_response

from core.spawn_egg import *

app = Flask(__name__)

""" # Função para modificar a imagem (por exemplo, redimensionar)
def modify_image():
    # Abrir a imagem
    with Image.open('src/assets/spawn_egg_base.png') as base_image:
        base_image = base_image.resize((128, 128), Image.NEAREST)
        
        with Image.open('src/assets/spawn_egg_overlay.png') as overlay_image:
          overlay_image = overlay_image.resize((128, 128), Image.NEAREST)
          position =  ((base_image.width - overlay_image.width) // 2, (base_image.height - overlay_image.height) // 2)
          base_image.paste(overlay_image, position, overlay_image)

        # Salvar a imagem modificada em um buffer
        buffer = io.BytesIO()
        base_image.save(buffer, format="PNG")
        buffer.seek(0)
        
        return buffer """

@app.route('/')
@app.route('/<base_color>')
@app.route('/<base_color>/<overlay_color>')
def display_image(base_color = '#FFFFFF', overlay_color = '#000000'):
    print(f'BASE_COLOR: {base_color} | OVERLAY_COLOR: {overlay_color}')

    # Obter a imagem modificada em um buffer
    image_buffer = SpawnEgg(base_color, overlay_color).get_mounted_spawn_egg_buffer()
    
    # Criar uma resposta HTTP com a imagem
    response = make_response(image_buffer.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'inline', filename='modified_image.png')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)