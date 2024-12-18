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

@app.route('/frame')
def frame():
    return render_template('frame.html')

# flask-bootstrap
@app.route('/it')
def informacijske_tehnologije():
    title = 'Informacijske tehnologije'
    return render_template('index.html', var=var, title=title, links_it=links_it)

link1 = '/opsus'
link2 = '/sjwp_1'
link3 = '/react-native'
link4 = '/wd_1'

subject1 = 'Operacijski sustavi'
subject2 = 'Skriptni jezici i web programiranje 1'
subject3 = 'Programiranje mobilnih uređaja'
subject4 = 'Web dizajn 1'

# 3. razred
# flask-bootstrap
@app.route('/opsus')
def operacijski_sustavi():
    title = 'Operacijski sustavi'  
    return render_template('index.html', 
                            var=var,
                            title=title, 
                            link1=link1, 
                            link2=link2, 
                            link3=link3, 
                            link4=link4,
                            subject1=subject1,
                            subject2=subject2,
                            subject3=subject3,
                            subject4=subject4,
                            links_it=links
                            )

# flask-bootstrap
@app.route('/sjwp_1')
def skriptni_jezici_i_web_programiranje_1():
    title = 'Skriptni jezici i web programiranje 1'    
    return render_template('index.html', 
                            var=var, 
                            title=title, 
                            link1=link1, 
                            link2=link2, 
                            link3=link3, 
                            link4=link4,
                            subject1=subject1,
                            subject2=subject2,
                            subject3=subject3,
                            subject4=subject4,
                            links_it=links_sjwp_n
                            )

# flask-bootstrap
@app.route('/wd_1')
def web_dizajn_1():
    title = 'Web dizajn'   
    return render_template('index.html', 
                            var=var, 
                            title=title, 
                            link1=link1, 
                            link2=link2, 
                            link3=link3, 
                            link4=link4,
                            subject1=subject1,
                            subject2=subject2,
                            subject3=subject3,
                            subject4=subject4,
                            links_it=links_web_dizajn_3
                            )

# flask-bootstrap
@app.route('/react-native')
def react_native():
    title = 'Programiranje mobilnih uređaja'   
    return render_template('index.html', 
                            var=var, 
                            title=title, 
                            link1=link1, 
                            link2=link2, 
                            link3=link3, 
                            link4=link4,
                            subject1=subject1,
                            subject2=subject2,
                            subject3=subject3,
                            subject4=subject4,
                            links_it=links_react_native
                            )

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=4000)