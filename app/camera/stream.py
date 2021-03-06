import cv2
import os
from typing import Generator

WEBCAM_INDEX = os.environ.get("WEBCAM_INDEX", None) or 0
CAMERA = cv2.VideoCapture(WEBCAM_INDEX)
CAMERA.set(3, os.environ.get("WEBCAM_WIDTH") or 640)
CAMERA.set(4, os.environ.get("WEBCAM_HEIGHT") or 360)
CAMERA.set(5, os.environ.get("WEBCAM_FPS") or 30)


def stream_generator() -> Generator[bytes, None, None]:
    while True:
        success, frame = CAMERA.read()
        if not success:
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
