from flask import Flask, render_template

app = Flask(__name__, static_folder='../home-page/docs/static', template_folder='../home-page/docs')

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()