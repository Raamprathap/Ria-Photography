from flask import Flask, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os
from urllib.parse import quote
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__, template_folder='templates')
CORS(app)

IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), 'image')

@app.route('/')
def index():
    return render_template('video.html')

@app.route('/get-images', methods=['GET'])
def get_images():
    try:
        image_filenames = []
        for filename in os.listdir(IMAGE_FOLDER):
            if filename.endswith(('.mp4')):
                image_url = f'/films/images/{quote(filename)}'
                image_filenames.append({"id": filename, "name": filename, "url": image_url})
        return jsonify(image_filenames)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/images/<path:filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/get-images', methods=['OPTIONS'])
def options_get_images():
    return '', 200

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
