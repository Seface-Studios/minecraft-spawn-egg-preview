from flask import Flask, send_from_directory, render_template, make_response
from core.spawn_egg import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route('/<base_color>/<overlay_color>', methods=['GET'])
@app.route('/<base_color>', defaults={ 'overlay_color': '000000' }, methods=['GET'])
def display_image(base_color, overlay_color):
    print(f'BASE_COLOR: {base_color} | OVERLAY_COLOR: {overlay_color}')

    spawn_egg = SpawnEgg(base_color, overlay_color)
    image_buffer = spawn_egg.get_mounted_spawn_egg_buffer()
    
    response = make_response(image_buffer.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'inline', filename=f'{spawn_egg.get_uuid()}.png')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)