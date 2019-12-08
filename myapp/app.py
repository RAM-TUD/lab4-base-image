from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


def contact():
    return <a href="mailto:name@email.com">Link text</a>
@app.add_url_rule("/contact","contact",contact)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80)
    
