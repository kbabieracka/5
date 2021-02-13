from flask import Flask, request , render_template

app = Flask(__name__)

@app.route('/')
def do_count():
    age = request.form['age']
    pig_age = age * 8.4
    return render_template('kalkulatorwieku2.html', thepig_age=pig_age)


app.run(debug=True)