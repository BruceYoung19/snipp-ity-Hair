from flask import Flask,render_template,request,jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def base():
    file_path = os.path.join('static/json','setup.json')
    load_json_data(file_path)
    return render_template('home.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

def load_json_data(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
            print(data)
        return data
    
    except FileNotFoundError:
        print(f"File not found at{file_path}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
