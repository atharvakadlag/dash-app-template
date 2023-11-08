from dash import Input, Output
import pandas as pd

from .graph import init_graph_callbacks


def init_callbacks(app):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

    @app.callback(
        Output('dropdown-selection', 'options'),
        Input('dummy-first-load-callbacks', 'children')
    )
    def initial_load(_):
        return df.country.unique()

    init_graph_callbacks(app, df)
