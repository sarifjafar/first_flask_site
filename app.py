from flask import Flask,render_template

host = '127.0.0.1'
port = 8000

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host=host,port=port,debug=True)

