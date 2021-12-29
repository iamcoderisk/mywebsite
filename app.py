# app.py
from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    now = datetime.datetime.now()
    return render_template('index.html',currentDate = now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    app.run(debug=True)



## ... source file continues with no further render_template examples...
