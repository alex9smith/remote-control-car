# Remote control car

Drive a toy car from a browser, with a bit of help from a Raspberry Pi.

## Requirements

A Raspberry Pi with `opencv-python` and all OS dependencies installed, and a USB webcam.

## Getting started

1. Make a python 3 virtual environment `python3 -m venv venv`. I recommend using `pyenv` to manage python versions
2. Set the  `WEBCAM_INDEX` environment variable if you have more than one camera connected
3. Set the `PORT` environment variable (defaults to `8081`)
4. Start the server by running `run.sh`
5. Go to `localhost:8081` in your browser (or substitute `localhost` for your Pi's IP)

