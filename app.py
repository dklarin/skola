from flask import Flask, render_template
from links import links
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('cs-for.html', links=links)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=4000)