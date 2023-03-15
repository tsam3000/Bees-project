from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def generic_route(page_name):
    return render_template(page_name)
