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

@app.route('/interactive_plot')
def interactive_plot():
    return render_template('interactive_plot.html')

if __name__ == '__main__':
    app.run()
