import json

import pandas as pd
import plotly
import plotly.graph_objects as go
from PIL import Image

data_mat = pd.read_csv("datas/data_mat.csv", index_col=0)
data_elec = pd.read_csv("datas/data_elec.csv", index_col=0)
data_eau = pd.read_csv("datas/data_eau.csv", index_col=0)

img = Image.open('static/img/le-présage-3D.png')


def config(data):
    index_list = data.index.tolist()
    n = len(index_list)
    buttons = []
    for k in range(n):
        visible = [False for k in range(n)]
        visible[k] = True
        title, label = index_list[k], index_list[k]
        buttons.append(
            dict(label=label,
                 method="update",
                 args=[{"visible": visible},
                       {"title": title,
                        "annotations": []}])

        )

    updatemenus = [
        dict(
            active=0,
            buttons=buttons
        )]
    data_list = data_mat.values.tolist()
    return n, data_list, index_list, updatemenus


def fig_matieres(data=data_mat):
    n, data_list, index, updatemenus = config(data)

    fig = go.Figure()

    fig.add_trace(
        go.Sankey(
            name=index[0],
            valueformat=".0f",
            valuesuffix="kg/jour",
            arrangement="snap",
            textfont={"size": 15,
                      "color": "black"},
            node={
                "label": ["Importations", "Valorisation matière et organique", "Le Présage", "Déchets",
                          "Gaz à effet de serre"],
                "x": [0.05, 0.5, 0.5, 0.95, 0.95],
                "y": [0.5, 0.6, 0.5, 0.9, 0.1],
                "thickness": 1,
                'hoverinfo': 'none',
                "color": ["#668C4A", "#A6BF4B", '#FFFFFF', "#AD724C", "#2B4B61"],
                # "hoverlabel": {"font": {"size": 15}},
                'pad': 80},  # 10 Pixels
            link={
                "source": [0, 2, 1, 2],
                "target": [2, 3, 1, 4],
                "value": data_list[0],
                "label": ["Importations", "Déchets", "Valorisation matière et organique", "Gaz à effet de serre"],
                "color": ["#668C4A", "#AD724C", "#A6BF4B", "#2B4B61"],
                "hoverlabel": {"font": {"size": 15}}
            }
        )
    )

    for k in range(1, n):
        fig.add_trace(
            go.Sankey(
                name=index[k],
                visible=False,
                valueformat=".0f",
                valuesuffix="kg/jour",
                arrangement="snap",
                textfont={"size": 15,
                          "color": "black"},
                node={
                    "label": ["Importations", "Valorisation matière et organique", "Le Présage", "Déchets",
                              "Gaz à effet de serre"],
                    "x": [0.05, 0.5, 0.5, 0.95, 0.95],
                    "y": [0.5, 0.6, 0.5, 0.9, 0.1],
                    "color": ["#668C4A", "#A6BF4B", '#FFFFFF', "#AD724C", "#2B4B61"],
                    "thickness": 1,
                    # "hoverlabel": {"font": {"size": 15}},
                    'hoverinfo': 'none',
                    'pad': 80},  # 10 Pixels
                link={
                    "source": [0, 2, 1, 2],
                    "target": [2, 3, 1, 4],
                    "value": data_list[0],
                    "label": ["Importations", "Déchets", "Valorisation matière et organique", "Gaz à effet de serre"],
                    "color": ["#668C4A", "#AD724C", "#A6BF4B", "#2B4B61"],
                    "hoverlabel": {"font": {"size": 15}}
                }
            )
        )

    fig.update_layout(updatemenus=updatemenus)
    fig.update_layout(autosize=True)

    fig.add_layout_image(
        dict(
            source=img,
            x=0.72,
            y=1.35,
            layer="above",
            xref="paper",
            yref="paper",
            sizex=1.5,
            sizey=1.5,
            xanchor="right",
            yanchor="top"
        )
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def fig_elec(data=data_elec):
    n, data_list, index, updatemenus = config(data)

    fig = go.Figure()
    fig.add_trace(
        go.Sankey(
            name=index[0],
            valueformat=".0f",
            valuesuffix="Wh/jour",
            arrangement="fixed",
            textfont={"size": 15,
                      "color": "black"},
            node={
                "label": ["Importation EDF", "Ensoleillement total", "Ensoleillement sur le four solaire",
                          "Le Présage"],
                "x": [0.1, 0.1, 0.1, 0.7],
                "y": [0.1, 0.5, 0.9, 0.5],
                'hoverinfo': 'none',
                "thickness": 1,
                "color": ["#AD724C", "#EDA20C", "#EDC00C", "#FFFFFF"],
                'pad': 80},  # 10 Pixels
            link={
                "source": [0, 1, 2],
                "target": [3, 3, 3],
                "value": data_list[0],
                "hoverlabel": {"font": {"size": 15}},
                "label": ["Consomnation EDF", "Consomnation energie verte"],
                "color": ["#AD724C", "#EDA20C", "#EDC00C"],

            }
        )
    )
    for k in range(1, n):
        fig.add_trace(
            go.Sankey(
                name=index[k],
                valueformat=".0f",
                valuesuffix="Wh/jour",
                arrangement="fixed",
                visible=False,
                textfont={"size": 15,
                          "color": "black"},
                node={
                    "label": ["Importation EDF", "Ensoleillement total", "Ensoleillement sur le four solaire",
                              "Le Présage"],
                    "x": [0.1, 0.1, 0.1, 0.7],
                    "y": [0.1, 0.5, 0.9, 0.5],
                    'hoverinfo': 'none',
                    "color": ["#D69D00", "#EDA20C", "#EDC00C", "#FFFFFF"],
                    "thickness": 1,
                    'pad': 80},  # 10 Pixels
                link={
                    "source": [0, 1, 2],
                    "target": [3, 3, 3],
                    "value": data_list[k],
                    "hoverlabel": {"font": {"size": 15}},
                    "label": ["Importation EDF", "Ensoleillement total", "Ensoleillement sur le four solaire"],
                    "color": ["#AD724C", "#EDA20C", "#EDC00C"],

                }
            )
        )

    fig.update_layout(updatemenus=updatemenus)

    fig.add_layout_image(
        dict(
            source=img,
            x=1,
            y=1.3,
            layer="above",
            xref="paper",
            yref="paper",
            sizex=1.5,
            sizey=1.5,
            xanchor="right",
            yanchor="top"
        ))

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def fig_eaux(data=data_eau):
    n, data_list, index, updatemenus = config(data)
    fig = go.Figure()
    fig.add_trace(
        go.Sankey(
            name=index[0],
            valueformat=".0f",
            valuesuffix="Litre/jour",
            arrangement="fixed",
            visible=True,
            textfont={"size": 15,
                      "color": "black"},
            node={
                "label": ["Eaux importées", "Eaux tombé", "Le Présage"],
                "x": [0.1, 0.1, 0.9],
                "y": [0.3, 0.7, 0.5],
                "color": ["#423DE6", "#4C95E6", "#FFFFFF"],
                "thickness": 1,
                'hoverinfo': 'none',
                'pad': 160},  # 10 Pixels
            link={
                "source": [0, 1],
                "target": [2, 2],
                "value": data_list[0],
                "label": ["Eaux importées", "Eaux tombé"],
                "color": ["#423DE6", "#4C95E6"],

            }
        )
    )
    for k in range(1, n):
        fig.add_trace(
            go.Sankey(
                name=index[k],
                valueformat=".0f",
                valuesuffix="Litre/jour",
                arrangement="fixed",
                visible=False,
                textfont={"size": 15,
                          "color": "black"},
                node={
                    "label": ["Eaux importées", "Eaux tombé", "Le Présage"],
                    "x": [0.1, 0.1, 0.9],
                    "y": [0.3, 0.7, 0.5],
                    "color": ["#423DE6", "#4C95E6", "#FFFFFF"],
                    "thickness": 1,
                    'hoverinfo': 'none',
                    'pad': 160},  # 10 Pixels
                link={
                    "source": [0, 1],
                    "target": [2, 2],
                    "value": data_list[k],
                    "label": ["Eaux importées", "Eaux tombé"],
                    "color": ["#423DE6", "#4C95E6"],

                }
            )
        )

    fig.update_layout(updatemenus=updatemenus)

    fig.add_layout_image(
        dict(
            source=img,
            x=1.1,
            y=1.3,
            layer="above",
            xref="paper",
            yref="paper",
            sizex=1.5,
            sizey=1.5,
            xanchor="right",
            yanchor="top"
        ))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
