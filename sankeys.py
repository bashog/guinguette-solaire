import pandas as pd
import plotly.graph_objects as go
from PIL import Image

data_mat = pd.read_csv("datas/data_mat.csv", index_col=0)
data_energ = pd.read_csv("datas/data_energ.csv", index_col=0)
data_eau = pd.read_csv("datas/data_eau.csv", index_col=0)

img = Image.open('static/img/le-présage-3D.png')


def config(data):
    unite = data.iloc[0].values.tolist()
    data = data.drop("Unité", inplace=False)
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
    data_list = data.values.tolist()
    return n, data_list, index_list, unite, updatemenus


def config_label(label_name, data_list, unite):
    m, n = len(label_name), len(data_list)
    label = []
    for i in range(n):
        temp = []
        for j in range(m):
            st = label_name[j] + " : " + str(data_list[i][j]) + " " + unite[j]
            temp.append(st)
        temp.append("")
        label.append(temp)
    return label


def fig_matieres(data=data_mat):
    n, data_list, index, unite, updatemenus = config(data)
    label_name = ["Importations", "Déchets", "Valorisation matière et organique", "Gaz à effet de serre"]
    label = config_label(label_name, data_list, unite)
    fig = go.Figure()

    fig.add_trace(
        go.Sankey(
            name=index[0],
            valueformat=".0f",
            valuesuffix="kg/jour",
            arrangement="snap",
            textfont={"size": 13,
                      "color": "black"},
            node={
                "label": label[0],
                "x": [0.05, 0.95, 0.5, 0.95, 0.5],
                "y": [0.5, 0.9, 0.6, 0.1, 0.5],
                "thickness": 1,
                'hoverinfo': 'none',
                "color": ["#668C4A", "#A6BF4B", '#FFFFFF', "#AD724C", "#2B4B61"],
                # "hoverlabel": {"font": {"size": 15}},
                'pad': 80},  # 10 Pixels
            link={
                "source": [0, 4, 2, 4],
                "target": [4, 1, 2, 3],
                "value": data_list[0],
                'hoverinfo': 'none',
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
                textfont={"size": 13,
                          "color": "black"},
                node={
                    "label": label[k],
                    "x": [0.05, 0.95, 0.5, 0.95, 0.5],
                    "y": [0.5, 0.9, 0.6, 0.1, 0.5],
                    "thickness": 1,
                    'hoverinfo': 'none',
                    "color": ["#668C4A", "#A6BF4B", '#FFFFFF', "#AD724C", "#2B4B61"],
                    # "hoverlabel": {"font": {"size": 15}},
                    'pad': 80},  # 10 Pixels
                link={
                    "source": [0, 4, 2, 4],
                    "target": [4, 1, 2, 3],
                    "value": data_list[k],
                    'hoverinfo': 'none',
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
    return fig


def fig_energ(data=data_energ):
    n, data_list, index, unite, updatemenus = config(data)
    label_name = ["Importation EDF", "Ensoleillement total", "Ensoleillement sur le four solaire"]
    label = config_label(label_name, data_list, unite)

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
                "label": label[0],
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
                'hoverinfo': 'none',
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
                    "label": label[k],
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
                    'hoverinfo': 'none',
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
    return fig


def fig_eaux(data=data_eau):
    n, data_list, index, unite, updatemenus = config(data)
    label_name = ["Eaux importées", "Eaux tombé"]
    label = config_label(label_name, data_list, unite)

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
                "label": label[0],
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
                'hoverinfo': 'none',
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
                    "label": label[k],
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
                    'hoverinfo': 'none',
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
    return fig


def intoJSON(fig):
    graphJSON = fig.to_json()
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
