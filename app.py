from flask import Flask, render_template
app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')

# Control structures - for
@app.route("/for/")
def cs_for():
    links = ['https://carnet-my.sharepoint.com/:b:/g/personal/danijel_klarin_skole_hr/EcnuvNGqQolHuclIkDsD7UwB5ASsPrBx6XXigbQjW7TUag?e=q1fsQU', 
             'https://carnet-my.sharepoint.com/:b:/g/personal/danijel_klarin_skole_hr/EeKg_7A-TW1Cp8nw7P8Py2cBxEJ2qi2rDsnnf2Gz3Zj_Fw?e=7Yyiug', 'Nije loše']
    return render_template('cs-for.html', links=links)