from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def guide(name=None):
    return render_template('patho.html', name=name)

