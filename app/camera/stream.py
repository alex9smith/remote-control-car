import cv2
from typing import Generator

WEBCAM_INDEX = 0
CAMERA = cv2.VideoCapture(WEBCAM_INDEX)


def stream_generator() -> Generator[bytes, None, None]:
    while True:
        success, frame = CAMERA.read()
        if not success:
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')