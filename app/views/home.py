from flask import Blueprint, Response, render_template
from app.camera.stream import stream_generator

home = Blueprint("home", __name__, url_prefix="")


@home.route("/")
def home_page():
    return render_template("home.html")


@home.route("/video-stream")
def video_stream():
    return Response(stream_generator(), mimetype='multipart/x-mixed-replace; boundary=frame')
