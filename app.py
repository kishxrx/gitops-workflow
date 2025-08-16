from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_devops():
    # Future idea: This could show a new DevOps quote on every refresh!
    return '<h1>GitOps Workflow: In Progress!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
