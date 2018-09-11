from my_app.config import settings, assets
from flask import Flask,jsonify
# set up the flask app

app = Flask(__name__, static_folder= "my_app/static",
            template_folder="my_app/templates")
assets.init_assets(app)
from my_app.controllers.home import *





if __name__ == "__main__":
    app.run(debug=app.debug, port=5001)
    setup_logging(logging_path=settings.LOGGING_PATH,
                  level=settings.LOGGING_LEVEL)
