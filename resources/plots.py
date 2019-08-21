import plotly
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import json

def create_plot(N, title="Grafiek Titel"):
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    fig = go.Figure(data=[
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ])

    fig.update_layout(title_text=title)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON