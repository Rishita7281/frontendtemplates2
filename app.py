from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video-dehazing-endpoint', methods=['POST'])
def video_dehazing_endpoint():
    if 'video' not in request.files:
        return 'No video file provided', 400

    video_file = request.files['video']

    
    # For now, just return a success message
    return 'Video dehazing successful'

if __name__ == '__main__':
    app.run(debug=True)
