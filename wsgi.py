import flask
from app.main import create_app

server = flask.Flask(__name__)

app = create_app(server=server)

app.server.run()
