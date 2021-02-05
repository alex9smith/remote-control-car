source venv/bin/activate
pip install -r requirements.txt
FLASK_APP="app" FLASK_ENV="development" flask run -h localhost -p 8081