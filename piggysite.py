from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/wpis")
def wpis():
    return render_template("wpis.html")

@app.route("/wpis1")
def wpis1():
    return render_template("wpis1.html")




if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run(debug=True)

