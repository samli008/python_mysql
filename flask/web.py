from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
  name={'username': 'root'}
  rows=[
    {'name': 'liyang','phone': '18116583538','age': 40},
    {'name': 'liyang','phone': '18116583538','age': 40},
    {'name': 'liyang','phone': '18116583538','age': 40},
    {'name': 'liyang','phone': '18116583538','age': 40},
  ]
  return render_template('index.html',name=name,rows=rows,title='sam')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
