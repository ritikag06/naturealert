from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/droughts')
def droughts():
    return render_template('droughts.html')

@app.route('/fires')
def fires():
    return render_template('fires.html')

# @app.route('/map')
# def map():
#     return render_template('map.html')

@app.route('/droughtplot')
def droughtplot():
    return render_template('interactive_graph.html')

if __name__ == '__main__':
    app.run()
