from flask import Flask, render_template
from links import *
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('cs-for.html', links_it=links_it,links=links, links_sjwp_u=links_sjwp_u, links_sjwp_n=links_sjwp_n)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=4000)