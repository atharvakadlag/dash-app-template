from dash import Output, Input
import plotly.express as px


def init_graph_callbacks(app, df):
    @app.callback(
        Output('graph-content', 'figure'),
        Input('dropdown-selection', 'value')
    )
    def update_graph(value):
        dff = df[df.country == value]
        return px.line(dff, x='year', y='pop')
