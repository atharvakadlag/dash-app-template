from dash import html

from .graph import init_graph_layout


def init_layout(app):
    app.layout = html.Div([
        html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
        init_graph_layout(app),
        # trigger stuff when app loads for the first time
        html.Div(id='dummy-first-load-callbacks')
    ])
