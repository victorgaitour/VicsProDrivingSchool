from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
app = Flask('__name__')
app.config['SECRET_KEY'] = "Alex is great"

@app.route("/", methods = ["POST", "GET"])
@app.route("/home", methods = ["POST", "GET"])
def home():
    return render_template("index.html")




if __name__=="__main__":
    app.debug = True
    app.run(port=8000)

