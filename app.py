import pandas as pd
import numpy as np
from dash import Dash, dcc, html

avocado_prices = pd.read_csv("avocado.csv", header=0).assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d").dt.date).query("type == 'conventional' and region == 'Albany'").sort_values("Date")

app = Dash(__name__)

server = app.server

app.layout = html.Div(
    children=[

        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": avocado_prices["Date"],
                                    "y": avocado_prices["AveragePrice"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Average Price of Avocados",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),

            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__": app.run(debug=True)