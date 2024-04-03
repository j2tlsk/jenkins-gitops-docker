from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Jale, ArgoCD sure is Cool but a little bit slow !!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
