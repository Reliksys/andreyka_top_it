from flask import Flask, render_template, url_for
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/ckebob')
def about():
    return render_template("ckebob.html")

@app.route('/achievments')
def achievments():
    return render_template("achievments.html")

@app.route('/letter')
def letter():
    return render_template("letter.html")

@app.route('/essay')
def essay():
    return render_template("essay.html")


if __name__ == "__main__":
    app.run(debug=True)