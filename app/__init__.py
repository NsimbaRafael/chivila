from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)

from app import routes