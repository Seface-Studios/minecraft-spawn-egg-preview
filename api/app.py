from flask import Flask, request, redirect, make_response, jsonify
from core.spawn_egg import *
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.sefacestudios.net')

@app.route('/<int:size>/<base_color>/<overlay_color>', methods=['GET'])
@app.route('/<base_color>/<overlay_color>', defaults={ 'size': 128 }, methods=['GET'])
def display_image(size: int, base_color: str, overlay_color: str):
    spawn_egg = SpawnEgg(size, base_color, overlay_color)
    image_buffer = spawn_egg.get_mounted_spawn_egg_buffer()
    
    return_data = request.args.get('data', 'false').lower() == 'true'

    if (return_data):
        return jsonify(spawn_egg.get_data())

    response = make_response(image_buffer.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'inline', filename=spawn_egg.filename)
    
    return response

if __name__ == '__main__': 
    app.run()
    