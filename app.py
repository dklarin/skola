from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from links import *

app = Flask(__name__)
bootstrap = Bootstrap(app)

var = "https://carnet-my.sharepoint.com/:b:/g/personal/danijel_klarin_skole_hr/"


@app.route("/frame")
def frame():
    return render_template("frame.html")

info = "Info stranica"
opsus = "Operacijski sustavi"
sjwp1 = "Skriptni jezici i web programiranje 1"
pmu1 = "Programiranje mobilnih uređaja 1"

@app.route("/")
def index():
   
    return render_template(
        "info.html",
        var=var,
        title=info,     
        gornja_tablica=links_sjwp_1_kodovi,
        donja_tablica=info_lista,
    )

@app.route("/opsus")
def operacijski_sustavi():
    title1 = "Vježbe"
    title2 = "Vježbe"
    return render_template(
        "index.html",
        var=var,
        title=opsus,    
        title1=title1,
        title2=title2,
        gornja_tablica=links_opsus_vjezbe,
        donja_tablica={},
    )

# flask-bootstrap
@app.route("/sjwp_1")
def skriptni_jezici_i_web_programiranje_1():
    title1 = "Kôdovi za 1. i 2. mrežnu stranicu"
    title2 = "Literatura za 2. pisanu provjeru znanja"
    return render_template(
        "index.html",
        var=var,
        title=sjwp1,      
        title1=title1,
        title2=title2,
        gornja_tablica=links_sjwp_1_kodovi,
        donja_tablica=links_sjwp_1_literatura,
    )


@app.route("/pmu_1")
def programiranje_mobilnih_uredjaja_1():
    title1 = "Prezentacije"
    title2 = ""
    return render_template(
        "index.html",
        var=var,
        title=pmu1,       
        title1=title1,
        title2=title2,
        gornja_tablica=links_pmu_1_literatura,
        donja_tablica={},
    )


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=4000)
