from flask import Flask
from flask import render_template
import pymysql

app = Flask(__name__)

@app.route('/')

def hello():
  name={'username': 'root'}

  connection=pymysql.connect("192.168.20.161","root","liyang","liyang")
  cursor=connection.cursor(pymysql.cursors.DictCursor)

  sql="select * from person;"
  count=cursor.execute(sql)
  result=cursor.fetchall()

  cursor.close()
  connection.close()

  return render_template('index.html',name=name,rows=result,title='mysql')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
