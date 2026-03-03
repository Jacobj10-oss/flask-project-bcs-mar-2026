from flask import Flask
from routes.movies_bp import movies_bp

app = Flask(__name__)

@app.get("/")
def hello():
    return "<h1>Hello, World! 🎉 🔥</h1>"

app.register_blueprint(movies_bp,url_prefix="/api/movies")
