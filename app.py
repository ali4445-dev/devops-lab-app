from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello DevOps World . This is a simple Flask application for my Devops Lab Mid!  '

if __name__ == '__main__':
    app.run(debug=True)
