import sys, os
sys.path.append(os.path.abspath("."))

from flask import Flask
from flask.json import JSONEncoder
from config import Config
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.from_object(Config)

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix="/api/v1")

from app.docs import bp as docs_bp
app.register_blueprint(docs_bp, url_prefix="/docs")

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Starting server')

