from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/top')
def top():
    return render_template("top.html")

@app.route('/topmoviecode')
def topmoviecode():
    return render_template("learn/topmoviecode.html")

@app.route('/random')
def random():
    return render_template("random.html")

@app.route('/randommoviegeneratorcode')
def randommoviegeneratorcode():
    return render_template("learn/randommoviegeneratorcode.html")

@app.route('/quiz')
def quiz():
    return render_template("pages/quiz.html")

@app.route('/moviequizcode')
def moviequizcode():
    return render_template("learn/moviequizcode.html")

@app.route('/learn')
def learn():
    return render_template("pages/learn.html")

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5222")