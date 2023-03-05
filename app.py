from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "This is our first application."

if __name__=="__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=8010)
