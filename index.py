from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/static/style.css') 
def external_css():
    return send_file('style.css')

@app.route('/static/scr.js') 
def external_js():
    return send_file('scr.js')

@app.route('/img/azpili') 
def upload_img1():
    return send_file('./pics/azpili.jpg')

@app.route('/img/cech') 
def upload_img2():
    return send_file('./pics/cech.jpg')

@app.route('/img/cole') 
def upload_img3():
    return send_file('./pics/cole.jpg')

@app.route('/img/Drogba') 
def upload_img4():
    return send_file('./pics/Drogba.jpg')

@app.route('/img/fabregas') 
def upload_img5():
    return send_file('./pics/fabregas.jpg')

@app.route('/img/hazard') 
def upload_img6():
    return send_file('./pics/hazard.jpg')

@app.route('/img/kante') 
def upload_img7():
    return send_file('./pics/kante.jpg')

@app.route('/img/lampard') 
def upload_img8():
    return send_file('./pics/lampard.jpg')

@app.route('/img/luiz') 
def upload_img9():
    return send_file('./pics/luiz.jpg')

@app.route('/img/Terry') 
def upload_img10():
    return send_file('./pics/Terry.jpg')

@app.route('/img/zola') 
def upload_img11():
    return send_file('./pics/zola.jpg')

app.run(host="localhost", port=5000)