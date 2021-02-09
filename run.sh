source venv/bin/activate
pip install -r requirements.txt
FLASK_APP="app" FLASK_ENV="development" flask run --host=0.0.0.0 -p "${PORT:-8081}"