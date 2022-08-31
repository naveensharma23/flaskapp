from flask import Flask
  
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0',port=82)
