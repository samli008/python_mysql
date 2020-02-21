from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
  name={'username': 'root'}
  return render_template('index.html',name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
