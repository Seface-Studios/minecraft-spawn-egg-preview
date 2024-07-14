from flask import Flask, redirect, make_response
from app.spawn_egg import *

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.sefacestudios.net')

@app.route('/<base_color>/<overlay_color>', methods=['GET'])
def display_image(base_color, overlay_color):
    spawn_egg = SpawnEgg(base_color, overlay_color)
    image_buffer = spawn_egg.get_mounted_spawn_egg_buffer()
    
    response = make_response(image_buffer.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'inline', filename=f'{spawn_egg.get_uuid()}.png')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)