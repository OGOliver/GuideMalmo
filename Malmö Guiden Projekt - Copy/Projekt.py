from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sevardheter')
def sevardheter():
    return render_template('sevardheter.html')

@app.route('/boenden')
def boenden():
    return render_template('boenden.html')

@app.route('/restauranger')
def restauranger():
    return render_template('restauranger.html')

@app.route('/shopping')
def shopping():
    return render_template('shopping.html')

@app.route('/evenemang')
def evenemang():
    return render_template('evenemang.html')

@app.route('/uteliv')
def uteliv():
    return render_template('uteliv.html')

@app.route('/kultur')
def kultur():
    return render_template('kultur.html')

@app.route('/dolda-parlor')
def dolda_parlor():
    return render_template('dolda_parlor.html')

@app.route('/sport')
def sport():
    return render_template('sport.html')

if __name__ == '__main__':
    app.run(debug=True)
