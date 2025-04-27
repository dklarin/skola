from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from links import *

app = Flask(__name__)
bootstrap = Bootstrap(app)

var = 'https://carnet-my.sharepoint.com/:b:/g/personal/danijel_klarin_skole_hr/'

@app.route('/frame')
def frame():
    return render_template('frame.html')

link1 = '/sjwp_1'
link2 = '/pmu_1'

info = 'Info stranica'
subject1 = 'Skriptni jezici i web programiranje 1'
subject2 = 'Programiranje mobilnih uređaja 1'

# 3. razred
# flask-bootstrap
@app.route('/')
def index():
    title = '9.5.2025. - 2. pisana provjera iz Skriptnih jezika i web programiranja'  
    return render_template('info.html', 
                            var=var,
                            title=info, 
                            link1=link1, 
                            link2=link2,                           
                            subject1=subject1,
                            subject2=subject2,                           
                            links_it=links_sjwp_1_kodovi,
                            links_lit=info_lista
                            )

# flask-bootstrap
@app.route('/sjwp_1')
def skriptni_jezici_i_web_programiranje_1():    
    return render_template('index.html', 
                            var=var, 
                            title=subject1, 
                            link1=link1, 
                            link2=link2,                          
                            subject1=subject1,
                            subject2=subject2,                          
                            links_it=links_sjwp_1_kodovi,
                            links_lit=links_sjwp_1_literatura
                            )

@app.route('/pmu_1')
def programiranje_mobilnih_uredjaja_1():   
    return render_template('index.html', 
                            var=var, 
                            title=subject2, 
                            link1=link1, 
                            link2=link2,                           
                            subject1=subject1,
                            subject2=subject2,                           
                            links_it=links_sjwp_1_literatura,
                            links_lit=links_pmu_1_literatura
                            )


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=4000)