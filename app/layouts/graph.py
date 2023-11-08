from dash import dcc, html


def init_graph_layout(app):
    return html.Div([
        dcc.Dropdown(id='dropdown-selection'),
        dcc.Graph(id='graph-content')
    ])
