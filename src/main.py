from flask import Flask, render_template, make_response, redirect
from flask_misaka import Misaka
from core.spawn_egg import *

app = Flask(__name__)
Misaka(app)

@app.route('/')
def index():
    with open("src/static/content/index.md", 'r', encoding='utf-8') as arquivo:
        mkd_text = arquivo.read()
        return render_template('index.html', mkd_text=mkd_text)
    # return redirect('https://www.sefacestudios.net')

@app.route('/<base_color>/<overlay_color>', methods=['GET'])
@app.route('/<base_color>', defaults={ 'overlay_color': '000000' }, methods=['GET'])
def display_image(base_color, overlay_color):
    spawn_egg = SpawnEgg(base_color, overlay_color)
    image_buffer = spawn_egg.get_mounted_spawn_egg_buffer()
    
    response = make_response(image_buffer.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'inline', filename=f'{spawn_egg.get_uuid()}.png')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)