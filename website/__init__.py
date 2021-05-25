from flask import Flask



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '4ef687468850cf8f52e316bb06e5b481'

    from .websiteapp import websiteapp

    app.register_blueprint(websiteapp, url_prefix='/')

    return app