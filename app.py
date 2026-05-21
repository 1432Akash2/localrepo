from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is my basic Flask app."

@app.route('/about')
def about():
    print("This is the about page.")
    return "This is the about page."

if __name__ == '__main__':
    app.run(debug=True)