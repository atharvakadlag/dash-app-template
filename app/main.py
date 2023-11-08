"""
Run this file using `python -m app.main`
"""

from dash import Dash

from .callbacks import init_callbacks
from .layouts import init_layout


def create_app(server=None):
    if server:
        app = Dash(__name__, server=server)
    else:
        app = Dash(__name__)

    init_layout(app)
    init_callbacks(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
