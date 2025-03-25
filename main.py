from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/motor')
def storitve():
    return render_template('motor.html')

@app.route('/jermen')
def kontakt():
    return render_template('jermen.html')

@app.route('/motor')
def storitev1():
    return render_template('motor.html')

@app.route('/turbina')
def storitev2():
    return render_template('turbina.html')

@app.route('/storitev3')
def storitev3():
    return render_template('storitev3.html')

@app.route('/storitev4')
def storitev4():
    return render_template('storitev4.html')

@app.route('/storitev5')
def storitev5():
    return render_template('storitev5.html')

if __name__ == '__main__':
    app.run(debug=True)