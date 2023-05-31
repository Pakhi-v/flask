from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    #return 'Hello, World!'


if __name__ == "__main__":  #to run program in debug mode
    app.run(debug=True,port=8000)