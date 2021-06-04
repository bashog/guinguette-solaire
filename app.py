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
    graph_matieres = sankeys.fig_matieres()
    graph_elec = sankeys.fig_elec()
    graph_eaux = sankeys.fig_eaux()
    return render_template("exploration.html", graph_matieres=graph_matieres, graph_elec=graph_elec,
                           graph_eaux=graph_eaux)

@app.route("/exploration/matieres/")
def view_matieres():
    graph_matieres = sankeys.fig_matieres()
    return render_template("matieres.html",graph_matieres=graph_matieres)

@app.route("/exploration/electricite/")
def view_electricite():
    graph_elec = sankeys.fig_elec()
    return render_template("electricite.html", graph_elec=graph_elec)

@app.route("/exploration/eaux/")
def view_eaux():
    graph_eaux = sankeys.fig_eaux()
    return render_template("eaux.html",graph_eaux=graph_eaux)


if __name__ == '__main__':
    app.run()
