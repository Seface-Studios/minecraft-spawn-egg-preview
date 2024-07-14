import os
from flask import Flask, redirect, make_response
from dotenv import load_dotenv
from app.spawn_egg import *

load_dotenv()
app = Flask(__name__)
app.config['DEBUG'] = True if os.getenv('DEV_ENV') == 'true' else False

@app.route('/')
def index():
    return redirect('https://www.sefacestudios.net')

@app.route('/<int:size>/<base_color>/<overlay_color>', methods=['GET'])
@app.route('/<base_color>/<overlay_color>', defaults={ 'size': 128 }, methods=['GET'])
def display_image(size: int, base_color: str, overlay_color: str):
    spawn_egg = SpawnEgg(size, base_color, overlay_color)
    image_buffer = spawn_egg.get_mounted_spawn_egg_buffer()
    
    response = make_response(image_buffer.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'inline', filename=f'{spawn_egg.get_uuid()}.png')
    
    return response

if __name__ == '__main__':
    if (app.config['DEBUG']):
        print(f' * Use example: http://127.0.0.1:5000/8073FF/D4FF7A')
        
    app.run()
    