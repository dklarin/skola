from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from links import *
app = Flask(__name__)
bootstrap = Bootstrap(app)

var = 'https://carnet-my.sharepoint.com/:b:/g/personal/danijel_klarin_skole_hr/'

@app.route('/')
def index():
    return render_template('cs-for.html', 
                           var=var,
                           links_it=links_it,
                           links=links, 
                           links_sjwp_u=links_sjwp_u, 
                           links_sjwp_n=links_sjwp_n,
                           software=software,
                           web_dizajn=web_dizajn,
                           flask=flask
                           )

# flask-bootstrap
@app.route('/it')
def informacijske_tehnologije():
    title = 'Informacijske tehnologije'
    return render_template('index.html', var=var, title=title, links_it=links_it)

# flask-bootstrap
@app.route('/opsus')
def operacijski_sustavi():
    title = 'Operacijski sustavi'
    link1 = '/opsus'
    link2 = '/sjwp'
    link3 = '/pmu'
    link4 = '/wd'
    return render_template('index.html', 
                           var=var,
                           title=title, 
                           link1=link1, 
                           link2=link2, 
                           link3=link3, 
                           link4=link4,
                           links_it=links
                           )

# flask-bootstrap
@app.route('/sjwp')
def skriptni_jezici_i_web_programiranje():
    title = 'Skriptni jezici i web programiranje'
    link1 = '/opsus'
    link2 = '/sjwp'
    link3 = '/pmu'
    link4 = '/wd'
    return render_template('index.html', 
                           var=var, 
                           title=title, 
                           link1=link1, 
                           link2=link2, 
                           link3=link3, 
                           link4=link4,
                           links_it=links_sjwp_n
                           )

# flask-bootstrap
@app.route('/wd')
def web_dizajn():
    title = 'Web dizajn'
    link1 = '/opsus'
    link2 = '/sjwp'
    link3 = '/pmu'
    link4 = '/wd'
    return render_template('index.html', 
                           var=var, 
                           title=title, 
                           link1=link1, 
                           link2=link2, 
                           link3=link3, 
                           link4=link4,
                           links_it=web_dizajn_3
                           )

# flask-bootstrap
@app.route('/react-native')
def react_native():
    title = 'Programiranje mobilnih uređaja'
    return render_template('index.html', title=title, links_it=links)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=4000)