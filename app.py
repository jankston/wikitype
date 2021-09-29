from flask import Flask, render_template
import wikitype

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/go')
def type():
    return render_template('type.html')


if __name__ == '__main__':
    app.run(debug=True)