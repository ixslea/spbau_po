from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

"""Homepage"""
@app.route('/')
def root():
    return render_template(
        'index.html'
    )
@app.route('/about/')
def about_method():
    return render_template(
        'about.html'
    )



