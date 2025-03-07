from flask import Flask
app = Flask (__name__)
@app.route('/saludar')
def hola_mundo():
    return 'Hola Mundo'
@app.route('/despedir')
def adios_mundo():
    return 'adios Mundo cruel'
@app.route('/saltar')
def saltar_html():
    return '<h1 style="color:red">salte sobre ti</h1>'
@app.route('/golpear')
def golpear():
    return 'te golpee'
@app.route('/json')
def algo():
    return '{"nombre":"John"}'
@app.route('/xml')
def xml():
    return '<?xml version="1.0"?><nombre>john</nombre>'
if __name__=='__main__':
    app.run(host='0.0.0.0',
    debug=True)