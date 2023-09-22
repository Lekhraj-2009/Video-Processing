# Import Libraries below
import os
import cv2
from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename

# Define flask 
app = Flask(__name__)
@app.route('/')

# Define upload_form() and route the webapp 
def upload_form():
    return render_template("upload.html")

@app.route('/', methods=['POST'])

# Define upload_video() to get video in defined folder and route the webapp  
def upload_video():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/', filename))
    return render_template("upload.html", filename=filename)
    source = cv2.VideoCapture('static/' + filename)
    # Sizing Ratio - 4:3
    frame_width = int(source.get(3))
    frame_height = int(source.get(4))
    size = (frame_width, frame_height)
    result = cv2.VideoWriter('static/'+'blackandwhite.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size, 0)

    try:
        while True:
            status, frame_image = source.read()
            gray = cv2.cvtColor(frame_image, cv2.COLOR_RGB2GRAY)
            result.write(gray)
            video_file = 'blackandwhite.mp4'
    except:
        print('Completed reading all frames from the Video')

@app.route('/download')
def download_file():
    converted_video_path = 'static/blackandwhite.mp4'
    return send_file(converted_video_path, as_attachment=True)

@app.route('/display/')

# Define display_video() to Display video in defined folder and route the webapp  
def display_video(filename):
    return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run(debug=True)
