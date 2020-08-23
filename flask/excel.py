# install flask xlrd pandas python packages
pip3 install flask -i https://mirrors.aliyun.com/pypi/simple
pip3 install xlrd -i https://mirrors.aliyun.com/pypi/simple
pip3 install pandas -i https://mirrors.aliyun.com/pypi/simple

# display excel to web
from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def excel():
  df = pd.read_excel("./sog.xlsx")
  table_html = df.to_html()
  return f"""
    <html>
      <body>
        <h1>ip list</h1>
        <div>{table_html}</div>
      </body>
    </html>
  """

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
