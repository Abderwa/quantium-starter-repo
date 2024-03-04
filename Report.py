import pandas as pd
from dash import Dash, dcc, html, Input, Output
from plotly.express import line

data = pd.read_csv('sales_data.csv')

app = Dash(__name__)

COLORS = {
    "primary": "black",
    "secondary": "white",
    "font": "white"
}

data = data.sort_values(by="date")


# vesualization
def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return line_chart


visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data)
)

#Header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": "black",
        "border-radius": "20px"
    }
)

#Region
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",

    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "color": "white",
        "font-size": "150%"


    }
)

# define the region picker callback
@app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    # filter the dataset
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    # generate a new line chart with the filtered data
    figure = generate_figure(trimmed_data)
    return figure


# define the app layout
app.layout = html.Div(
    [
        header,
        visualization,
        region_picker_wrapper
    ],
    style={
        "textAlign": "center",
        "background-color": "blue",
        "border-radius": "20px"
    }
)



if __name__ == "__main__":
    app.run_server(debug=True)
