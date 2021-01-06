from flask import Flask, render_template, url_for, Response, redirect
from camera import VideoCamera

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def generate(camera):
    """Generate feed to display and encode"""
    while True:
        data = camera.get_frame()
        frame = data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route("/video_feed")
def video_feed():
    return Response(generate(VideoCamera()), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/webcam", methods=["GET", "POST"])
def webcam():
    # return redirect(url_for("video_feed"))
    return render_template("webcam.html")


if __name__ == "__main__":
    app.run()
