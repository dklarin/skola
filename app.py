from flask import Flask, render_template
from links import *
app = Flask(__name__)

var = 'https://carnet-my.sharepoint.com/:b:/g/personal/danijel_klarin_skole_hr/'

@app.route('/')
def index():
    return render_template('cs-for.html', var=var,links_it=links_it,links=links, links_sjwp_u=links_sjwp_u, links_sjwp_n=links_sjwp_n,software=software)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=4000)