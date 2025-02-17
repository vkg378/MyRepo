#main.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
#name index is only a convention
def index():
    return 'Hello World\n'
    #eturn 'congratulations, its a webapp'

#if __name__ == '__main__':
#    app.run(host='127.0.0.1',port=8080,debug=True)
