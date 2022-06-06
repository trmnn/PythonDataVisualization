import pandas as pd
from bokeh.io import output_file,show
from bokeh.plotting import figure


def create_graph(file_name :str) -> None:
    df = pd.read_csv(file_name)

    output_file("Graph.html")

    fig=figure(tools=["crosshair"],
               sizing_mode="stretch_width")
    fig.title.text="Percentage of women graduating from an engineering degree"
    fig.title.text_color="Gray"
    fig.title.text_font="times"
    fig.title.text_font_style="bold"
    fig.xaxis.minor_tick_line_color=None
    fig.yaxis.minor_tick_line_color=None
    fig.xaxis.axis_label="Date"
    fig.yaxis.axis_label="Percentage"
    fig.xaxis.ticker = df["Year"].tolist()
    fig.yaxis.ticker = list(range(0,22))
    fig.line(df["Year"],
             df["Engineering"],
             line_width=3)

    show(fig)

if __name__ == '__main__':
    create_graph("bachelors.csv")