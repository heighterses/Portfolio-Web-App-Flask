from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('contact.html')


@app.route("/login", methods=["POST"])
def data_receive():
        name = request.form["username"]
        password = request.form["password"]
        return f"<h1>name: {name}</h1>"

@app.route('/contact', methods=["POST"])
def contact_form():
    pass



if __name__ == '__main__':
    app.run()
