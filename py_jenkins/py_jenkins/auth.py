# @FileName: auth.py.py
# @Author  : Anthony Wang
from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return 'hello,test is ok'


if __name__ == '__main__':

    app.run()
