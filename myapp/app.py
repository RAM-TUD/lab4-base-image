from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!doctype html>
    <title>Reda</title>
    <h1>C17456666 DT228 Cloud Computing</h1>
    """

@app.route("/contact-me")
def email():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0' port=5000)
    
