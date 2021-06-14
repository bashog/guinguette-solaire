from flask import Flask, render_template

import sankeys

app = Flask(__name__)


@app.route("/")
@app.route('/accueil/')
def view_home():
    return render_template("index.html")

@app.route("/presentation-du-projet/")
def view_pres_proj():
    return render_template("presentation-du-projet.html")

@app.route("/exploration/")
def view_expl():
    graph_matieres = sankeys.intoJSON(sankeys.fig_matieres())
    graph_energ = sankeys.intoJSON(sankeys.fig_energ())
    graph_eaux = sankeys.intoJSON(sankeys.fig_eaux())
    return render_template("exploration.html", graph_matieres=graph_matieres, graph_energ=graph_energ,
                           graph_eaux=graph_eaux)

@app.route("/exploration/matieres/")
def view_matieres():
    graph_matieres = sankeys.intoJSON(sankeys.fig_matieres())
    return render_template("matieres.html",graph_matieres=graph_matieres)


@app.route("/exploration/energie/")
def view_energ():
    graph_energ = sankeys.intoJSON(sankeys.fig_energ())
    return render_template("energie.html", graph_energ=graph_energ)

@app.route("/exploration/eaux/")
def view_eaux():
    graph_eaux = sankeys.intoJSON(sankeys.fig_eaux())
    return render_template("eaux.html",graph_eaux=graph_eaux)


if __name__ == '__main__':
    app.run()
