from flask import Flask, render_template

app = Flask(__name__, static_folder='../home-page/docs/static', template_folder='../home-page/docs')

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


@app.route('/home-page/about')
def index2():
    name = "ブラウザバックを一回押した後、ページを更新して！Kappa"
    return name

if __name__ == '__main__':
    app.run()