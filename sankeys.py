import json

import pandas as pd
import plotly
import plotly.graph_objects as go
from PIL import Image

data_mat = pd.read_csv("datas/data_mat.csv", index_col=0)

img = Image.open('static/img/le-présage-3D.png')


def fig_matieres():
    fig = go.Figure(
        go.Sankey(
            valueformat=".0f",
            valuesuffix="kg/jour",
            arrangement="fixed",
            node={
                "label": ["Importations", "Valorisation matière et organique", "Le Présage", "Exportations"],
                "x": [0.1, 0.5, 0.5, 0.9],
                "y": [0.5, 0.8, 0.5, 0.5],
                "thickness": 1,
                'pad': 110},  # 10 Pixels
            link={
                "source": [0, 2, 1],
                "target": [2, 3, 1],
                "value": [2, 2, 1],
                "label": ["Importations", "Exportations", "Valorisation matière et organique"],

            }
        )
    )
    fig.add_layout_image(
        dict(
            source=img,
            x=0.78,
            y=0.05,
            layer="above",
            xref="paper",
            yref="paper",
            sizex=1.2,
            sizey=1.2,
            xanchor="right",
            yanchor="bottom"
        )
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def fig_energies():
    fig = go.Figure(
        go.Sankey(
            valueformat = ".0f",
            valuesuffix = "Wh/jour",
            arrangement="fixed",
            node={
                "label" : ["EDF","Energie verte", "Le Présage"],
                "x": [0.1, 0.1, 0.5],
                "y": [0.3, 0.7, 0.5],
                "thickness": 1,
                'pad': 110},  # 10 Pixels
            link={
                "source": [0, 1],
                "target": [2, 2],
                "value": [5, 2, 1],
                "label" : ["Consomnation EDF","Consomnation energie verte"],

            }
        )
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def fig_eaux():
    fig = go.Figure(
        go.Sankey(
            valueformat = ".0f",
            valuesuffix = "Litre/jour",
            arrangement="fixed",
            node={
                "label" : ["Eaux importées","Eaux collectées", "Le Présage","Sortie eaux"],
                "x": [0.1, 0.1, 0.5, 0.9],
                "y": [0.3, 0.7, 0.5, 0.5],
                "thickness": 1,
                'pad': 110},  # 10 Pixels
            link={
                "source": [0, 1, 2],
                "target": [2, 2, 3],
                "value": [2, 2, 3],
                "label" : ["Importations", "Exportations", "Valorisation matière et organique"],

            }
        )
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

