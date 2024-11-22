from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Import routes and models
    from . import routes
    #from . import models

    app.register_blueprint(routes.bp)

    return app
