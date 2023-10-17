from dash import Dash
from dash import dcc
from dash import html
import pandas as pd

data = pd.read_csv('sales_data.csv')

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Sales Analytics",),
        html.P(
            children="Analyze if sales are higher before or after the Pink Morsel price increase on the 15th of January, 2021?",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["date"],
                        "y": data["sales"],
                        "type": " lines",
                    },
                ],
                "layout": {"title": "sales"},

            },
        ),

    ]
)
if __name__ == "__main__":
    app.run_server(debug=True)
