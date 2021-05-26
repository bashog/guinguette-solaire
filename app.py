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
    graph_energies = sankeys.fig_energies()
    graph_eaux = sankeys.fig_eaux()
    return render_template("exploration.html", graph_matieres=graph_matieres, graph_energies=graph_energies, graph_eaux=graph_eaux)

@app.route("/exploration/matieres/")
def view_matieres():
    graph_matieres = sankeys.fig_matieres()
    return render_template("matieres.html",graph_matieres=graph_matieres)

@app.route("/exploration/energies/")
def view_energies():
    graph_energies = sankeys.fig_energies()
    return render_template("energies.html",graph_energies=graph_energies)

@app.route("/exploration/eaux/")
def view_eaux():
    graph_eaux = sankeys.fig_eaux()
    return render_template("eaux.html",graph_eaux=graph_eaux)



if __name__ == '__main__':
    app.run()
